import streamlit as st

def main():
    st.set_page_config(page_title="AIMLAB PRO: CORE ENGINE", layout="wide")

    # 🎨 에임 몰입도를 높이는 사이버 다크 테마
    st.markdown("""
        <style>
        .main { background-color: #08090c; color: #d1d5db; font-family: 'Segoe UI', monospace; }
        .stButton > button {
            background: linear-gradient(135deg, #00f2fe, #4facfe) !important;
            color: #08090c !important; font-weight: bold !important; border: none !important;
            padding: 12px; border-radius: 4px; width: 100%; letter-spacing: 1px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center; color:#00f2fe; font-weight:900; letter-spacing:1px;'>🎯 AIMLAB METRICS PRO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#4b5563; font-size:14px;'>레벨 시스템 및 리더보드가 탑재된 반응형 에임 트레이너</p>", unsafe_allow_html=True)

    # JavaScript 기반 고성능 훈련장 컴포넌트 이식
    html_src = """
    <div style="max-width:1150px; margin:0 auto; display:flex; gap:20px; justify-content:center;">
        
        <div style="flex: 1; text-align:center;">
            <div style="display:flex; justify-content:space-between; align-items:center; background:#111827; padding:12px 20px; border-radius:6px; margin-bottom:12px; border:1px solid #1f2937;">
                <div style="display:flex; gap:8px;">
                    <button onclick="changeMode('gridshot')" id="m-grid" style="background:#00f2fe; color:black; border:none; padding:8px 16px; font-weight:bold; cursor:pointer; border-radius:4px;">🎯 GRIDSHOT</button>
                    <button onclick="changeMode('tracking')" id="m-track" style="background:#08090c; color:#00f2fe; border:1px solid #00f2fe; padding:8px 16px; font-weight:bold; cursor:pointer; border-radius:4px;">🔄 TRACKING</button>
                </div>
                <div style="display:flex; gap:20px; font-family:monospace; font-size:15px; font-weight:bold;">
                    <div style="color:#00f2fe;" id="ui-score">SCORE: 0</div>
                    <div style="color:#34d399;" id="ui-acc">ACC: 100%</div>
                    <div style="color:#f87171;" id="ui-time">TIME: 30.0s</div>
                </div>
                <button onclick="startSession()" id="start-btn" style="background:#34d399; color:black; border:none; padding:8px 20px; font-weight:bold; cursor:pointer; border-radius:4px;">▶ 훈련 시작</button>
            </div>
            
            <canvas id="aimCanvas" width="840" height="500" style="background:#0b0f17; border:2px solid #1f2937; border-radius:6px; cursor:none;"></canvas>
        </div>

        <div style="width:280px; display:flex; flex-direction:column; gap:15px; text-align:left;">
            <div style="background:#111827; padding:16px; border-radius:6px; border:1px solid #1f2937;">
                <div style="color:#00f2fe; font-size:12px; font-weight:bold; letter-spacing:1px;">USER PROFILE</div>
                <div style="font-size:22px; font-weight:900; color:white; margin:5px 0;" id="prof-lvl">LV. 1</div>
                <div style="font-size:11px; color:#9ca3af; margin-bottom:4px;" id="prof-exp">EXP: 0 / 1000</div>
                <div style="width:100%; background:#1f2937; height:6px; border-radius:3px; overflow:hidden;">
                    <div id="exp-bar" style="width:0%; background:#00f2fe; height:100%; transition:0.3s;"></div>
                </div>
            </div>

            <div style="background:#111827; padding:16px; border-radius:6px; border:1px solid #1f2937; flex:1; display:flex; flex-direction:column;">
                <div style="color:#00f2fe; font-size:12px; font-weight:bold; letter-spacing:1px; margin-bottom:10px;">🏆 LOCAL LEADERBOARD</div>
                <div id="leaderboard-list" style="font-family:monospace; font-size:13px; display:flex; flex-direction:column; gap:8px; color:#e5e7eb;">
                    </div>
                <button onclick="clearLeaderboard()" style="margin-top:auto; background:transparent; color:#6b7280; border:1px solid #374151; padding:5px; font-size:11px; cursor:pointer; border-radius:4px;">기록 초기화</button>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('aimCanvas');
        const ctx = canvas.getContext('2d');

        // 상태 변수
        let mode = 'gridshot';
        let isPlaying = false;
        let score = 0;
        let timeLeft = 30.0;
        let totalShots = 0;
        let hitShots = 0;
        let mouseX = 420, mouseY = 250;

        // 레벨 및 저장 데이터
        let userLevel = 1;
        let userExp = 0;
        let highScores = { gridshot: 0, tracking: 0 };

        // 물리 연산 오브젝트
        let targets = [];
        let recoilActive = false;
        let recoilFrame = 0;

        // 초기 로컬 스토리지 데이터 로드
        function loadSavedData() {
            if(localStorage.getItem('aimlab_lvl')) userLevel = parseInt(localStorage.getItem('aimlab_lvl'));
            if(localStorage.getItem('aimlab_exp')) userExp = parseInt(localStorage.getItem('aimlab_exp'));
            if(localStorage.getItem('aimlab_hs')) highScores = JSON.parse(localStorage.getItem('aimlab_hs'));
            updateProfileUI();
            renderLeaderboard();
        }

        function saveData() {
            localStorage.setItem('aimlab_lvl', userLevel);
            localStorage.setItem('aimlab_exp', userExp);
            localStorage.setItem('aimlab_hs', JSON.stringify(highScores));
        }

        function updateProfileUI() {
            document.getElementById('prof-lvl').innerText = "LV. " + userLevel;
            let nextExp = userLevel * 1000;
            document.getElementById('prof-exp').innerText = "EXP: " + userExp + " / " + nextExp;
            document.getElementById('exp-bar').style.width = (userExp / nextExp * 100) + "%";
        }

        function renderLeaderboard() {
            const list = document.getElementById('leaderboard-list');
            list.innerHTML = `
                <div style="display:flex; justify-content:space-between; border-bottom:1px solid #374151; padding-bottom:4px; color:#9ca3af;">
                    <span>MODE</span><span>HIGH SCORE</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span>🎯 GRIDSHOT</span><span style="color:#00f2fe; font-weight:bold;">${highScores.gridshot}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span>🔄 TRACKING</span><span style="color:#00f2fe; font-weight:bold;">${highScores.tracking}</span>
                </div>
            `;
        }

        function clearLeaderboard() {
            highScores = { gridshot: 0, tracking: 0 };
            userLevel = 1; userExp = 0;
            saveData(); updateProfileUI(); renderLeaderboard();
        }

        function changeMode(m) {
            if(isPlaying) return; // 게임 중 모드 변경 차단
            mode = m;
            document.getElementById('m-grid').style.background = (m === 'gridshot') ? '#00f2fe' : '#08090c';
            document.getElementById('m-grid').style.color = (m === 'gridshot') ? 'black' : '#00f2fe';
            document.getElementById('m-track').style.background = (m === 'tracking') ? '#00f2fe' : '#08090c';
            document.getElementById('m-track').style.color = (m === 'tracking') ? 'black' : '#00f2fe';
            initTargets();
        }

        function initTargets() {
            targets = [];
            if(mode === 'gridshot') {
                for(let i=0; i<3; i++) targets.push(spawnTargetObject());
            } else {
                targets.push(spawnTargetObject());
            }
        }

        function spawnTargetObject() {
            return {
                x: 50 + Math.random() * (canvas.width - 100),
                y: 50 + Math.random() * (canvas.height - 100),
                radius: mode === 'gridshot' ? 18 : 22,
                vx: (Math.random() - 0.5) * 6,
                vy: (Math.random() - 0.5) * 6
            };
        }

        function startSession() {
            if(isPlaying) return;
            isPlaying = true;
            score = 0; timeLeft = 30.0; totalShots = 0; hitShots = 0;
            initTargets();
            document.getElementById('start-btn').style.background = '#4b5563';
            document.getElementById('start-btn').innerText = "⏱ 훈련 중...";
        }

        function endSession() {
            isPlaying = false;
            document.getElementById('start-btn').style.background = '#34d399';
            document.getElementById('start-btn').innerText = "▶ 훈련 시작";
            
            // 점수 기록 검증 및 리더보드 갱신
            if(score > highScores[mode]) {
                highScores[mode] = score;
            }
            
            // 경험치 지급 및 레벨업 연산
            userExp += Math.floor(score / 10);
            let nextExp = userLevel * 1000;
            if(userExp >= nextExp) {
                userExp -= nextExp;
                userLevel++;
            }
            
            saveData(); updateProfileUI(); renderLeaderboard();
        }

        canvas.addEventListener('mousemove', (e) => {
            let rect = canvas.getBoundingClientRect();
            mouseX = (e.clientX - rect.left) * (canvas.width / rect.width);
            mouseY = (e.clientY - rect.top) * (canvas.height / rect.height);
        });

        canvas.addEventListener('mousedown', () => {
            if(!isPlaying) return;

            totalShots++;
            recoilActive = true; recoilFrame = 0; // 격발 반동 트리거 활성화
            let hitAny = false;

            for(let i=0; i<targets.length; i++) {
                let dist = Math.hypot(mouseX - targets[i].x, mouseY - targets[i].y);
                if(dist <= targets[i].radius) {
                    hitShots++;
                    score += 100;
                    hitAny = true;
                    if(mode === 'gridshot') targets[i] = spawnTargetObject();
                    break;
                }
            }
            if(!hitAny && mode === 'gridshot') score = Math.max(0, score - 20);
            updateDashboard();
        });

        function updateDashboard() {
            document.getElementById('ui-score').innerText = "SCORE: " + score;
            let acc = totalShots > 0 ? Math.round((hitShots / totalShots) * 100) : 100;
            document.getElementById('ui-acc').innerText = "ACC: " + acc + "%";
            document.getElementById('ui-time').innerText = "TIME: " + timeLeft.toFixed(1) + "s";
        }

        function loop() {
            ctx.fillStyle = '#0b0f17'; ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 배경 스팅어 격자선 드로우
            ctx.strokeStyle = '#111827'; ctx.lineWidth = 1;
            for(let i=0; i<canvas.width; i+=40) { ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,canvas.height); ctx.stroke(); }
            for(let j=0; j<canvas.height; j+=40) { ctx.beginPath(); ctx.moveTo(0,j); ctx.lineTo(canvas.width,j); ctx.stroke(); }

            if(isPlaying) {
                timeLeft -= 1/60;
                if(timeLeft <= 0) { timeLeft = 0; endSession(); }
                updateDashboard();

                // 타겟 그리기 및 이동 물리 연산
                targets.forEach((t) => {
                    if(mode === 'tracking') {
                        t.x += t.vx; t.y += t.vy;
                        if(t.x - t.radius < 0 || t.x + t.radius > canvas.width) t.vx *= -1;
                        if(t.y - t.radius < 0 || t.y + t.radius > canvas.height) t.vy *= -1;

                        // 실시간 마우스 트래킹 유지 프레임 누적 점수 연산
                        let dist = Math.hypot(mouseX - t.x, mouseY - t.y);
                        if(dist <= t.radius) score += 2;
                    }

                    // 테크니컬 원형 과녁 렌더링
                    ctx.save();
                    ctx.strokeStyle = '#00f2fe'; ctx.lineWidth = 3;
                    ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI*2); ctx.stroke();
                    ctx.fillStyle = 'rgba(0, 242, 254, 0.1)'; ctx.fill();
                    ctx.restore();
                });
            } else {
                // 시작 대기 가이드라인 렌더링
                ctx.fillStyle = 'rgba(255,255,255,0.4)'; ctx.font = '15px sans-serif'; ctx.textAlign = 'center';
                ctx.fillText("상단의 [▶ 훈련 시작] 버튼을 누르면 세션이 개시됩니다.", canvas.width/2, canvas.height/2);
            }

            // 🛠️ 격발 반동 모션(Recoil) 연동형 조준선 계산
            ctx.save();
            ctx.strokeStyle = '#34d399'; ctx.lineWidth = 1.5;
            
            let gap = 3; // 평상시 에임 오므라짐 격차
            if(recoilActive) {
                recoilFrame++;
                // 발사 순간 십자선 벌어짐 수식 연산
                gap += Math.sin((recoilFrame / 8) * Math.PI) * 8;
                if(recoilFrame > 8) recoilActive = false;
            }

            ctx.beginPath();
            ctx.moveTo(mouseX - gap - 8, mouseY); ctx.lineTo(mouseX - gap, mouseY);
            ctx.moveTo(mouseX + gap, mouseY); ctx.lineTo(mouseX + gap + 8, mouseY);
            ctx.moveTo(mouseX, mouseY - gap - 8); ctx.lineTo(mouseX, mouseY - gap);
            ctx.moveTo(mouseX, mouseY + gap); ctx.lineTo(mouseX, mouseY + gap + 8);
            ctx.stroke();
            ctx.restore();

            requestAnimationFrame(loop);
        }

        // 초기 인스턴스 셋업 실행
        loadSavedData();
        initTargets();
        loop();
    </script>
    """
    st.components.v1.html(html_src, height=580)

if __name__ == "__main__":
    main()
