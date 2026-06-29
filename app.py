import streamlit as st

def main():
    st.set_page_config(page_title="FPS AIMLAB RAW MOVEMENT ENGINE", layout="wide")

    st.markdown("""
        <style>
        .main { background-color: #07080b; color: #e5e7eb; font-family: 'Segoe UI', monospace; }
        .stButton > button {
            background: linear-gradient(135deg, #00f2fe, #4facfe) !important;
            color: #07080b !important; font-weight: bold !important; border: none !important;
            padding: 12px; border-radius: 4px; width: 100%; letter-spacing: 1px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center; color:#00f2fe; font-weight:900;'>🎯 AIMLAB: RAW MOVEMENT ENGINE</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#4b5563; font-size:14px;'>iframe 보안 우회 적용형 정밀 감도 | 빨간 점 에임 | 난이도 레벨 제어 | 무반동</p>", unsafe_allow_html=True)

    html_src = """
    <div style="max-width:1240px; margin:0 auto; display:flex; gap:20px; justify-content:center;">
        
        <div style="flex: 1; text-align:center;">
            <div style="display:flex; justify-content:space-between; align-items:center; background:#111827; padding:12px 20px; border-radius:6px; margin-bottom:12px; border:1px solid #1f2937;">
                <div style="display:flex; gap:6px;">
                    <button onclick="changeMode('gridshot')" id="m-grid" style="background:#00f2fe; color:black; border:none; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">🎯 GRIDSHOT</button>
                    <button onclick="changeMode('tracking')" id="m-track" style="background:#07080b; color:#00f2fe; border:1px solid #00f2fe; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">🔄 TRACKING</button>
                    <button onclick="changeMode('microflex')" id="m-micro" style="background:#07080b; color:#00f2fe; border:1px solid #00f2fe; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">⚡ MICROFLEX</button>
                </div>
                <div style="display:flex; gap:20px; font-family:monospace; font-size:15px; font-weight:bold;">
                    <div style="color:#00f2fe;" id="ui-score">SCORE: 0</div>
                    <div style="color:#34d399;" id="ui-acc">ACC: 100%</div>
                    <div style="color:#f87171;" id="ui-time">TIME: 30.0s</div>
                </div>
                <button onclick="startSession()" id="start-btn" style="background:#34d399; color:black; border:none; padding:8px 18px; font-weight:bold; cursor:pointer; border-radius:4px;">▶ 훈련 시작</button>
            </div>
            
            <div style="position:relative;">
                <canvas id="aimCanvas" width="860" height="510" style="background:#090b11; border:2px solid #1f2937; border-radius:6px; cursor:none;"></canvas>
            </div>
        </div>

        <div style="width:280px; display:flex; flex-direction:column; gap:15px; text-align:left;">
            
            <div style="background:#111827; padding:16px; border-radius:6px; border:1px solid #1f2937;">
                <div style="color:#34d399; font-size:12px; font-weight:bold; letter-spacing:1px; margin-bottom:8px;">⚙️ REAL FPS SENSITIVITY</div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <span style="font-size:13px; color:#9ca3af;">조준선 감도 배율</span>
                    <span style="font-size:16px; font-weight:bold; color:#34d399; font-family:monospace;" id="sens-val">1.00</span>
                </div>
                <input type="range" id="sens-slider" min="0.1" max="4.0" step="0.05" value="1.0" oninput="updateSensitivity(this.value)" style="width:100%; accent-color:#34d399; cursor:pointer;">
                <div style="font-size:11px; color:#6b7280; margin-top:6px; line-height:1.4;">* 마우스 락 없이 브라우저 보안을 우회하여 마우스의 순수 움직임 변화량만 계산하는 동기화 모드입니다.</div>
            </div>

            <div style="background:#111827; padding:16px; border-radius:6px; border:1px solid #1f2937;">
                <div style="color:#00f2fe; font-size:12px; font-weight:bold; letter-spacing:1px; margin-bottom:12px;">🎚️ 난이도 레벨 설정</div>
                <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px;">
                    <button onclick="setDifficulty(1)" id="df-1" style="background:#22c55e; color:black; border:none; padding:10px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:13px;">레벨 1</button>
                    <button onclick="setDifficulty(2)" id="df-2" style="background:#07080b; color:#e5e7eb; border:1px solid #374151; padding:10px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:13px;">레벨 2</button>
                    <button onclick="setDifficulty(3)" id="df-3" style="background:#07080b; color:#e5e7eb; border:1px solid #374151; padding:10px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:13px;">레벨 3</button>
                    <button onclick="setDifficulty(4)" id="df-4" style="background:#07080b; color:#e5e7eb; border:1px solid #374151; padding:10px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:13px;">레벨 4</button>
                </div>
                <div style="margin-top:12px; font-size:12px; color:#9ca3af; line-height:1.5; background:#07080b; padding:10px; border-radius:4px;" id="df-desc">
                    <strong>🟢 레벨 1 사양:</strong><br>과녁 반경: 기본 1.3배 확대<br>이동 속도: 0.5배 감속
                </div>
            </div>

            <div style="background:#111827; padding:16px; border-radius:6px; border:1px solid #1f2937; flex:1; display:flex; flex-direction:column;">
                <div style="color:#00f2fe; font-size:12px; font-weight:bold; letter-spacing:1px; margin-bottom:10px;">🏆 PERSONAL RECORDS</div>
                <div id="record-board" style="font-family:monospace; font-size:13px; display:flex; flex-direction:column; gap:10px; color:#e5e7eb;">
                    </div>
                <button onclick="clearAllData()" style="margin-top:auto; background:transparent; color:#4b5563; border:1px solid #374151; padding:6px; font-size:11px; cursor:pointer; border-radius:4px; font-weight:bold;">기록 초기화</button>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('aimCanvas');
        const ctx = canvas.getContext('2d');

        // 상태 데이터 메커니즘
        let mode = 'gridshot';
        let difficulty = 1;
        let sensitivity = 1.0;
        let isPlaying = false;
        let score = 0;
        let timeLeft = 30.0;
        let totalShots = 0;
        let hitShots = 0;

        // 🎯 우회형 고정식 인게임 조준선 좌표 (화면 중심 시작)
        let mouseX = 430, mouseY = 255;
        
        // 이전 프레임의 실제 마우스 하드웨어 위치 기억용 변수
        let lastRealX = null;
        let lastRealY = null;

        let highScores = { gridshot: 0, tracking: 0, microflex: 0 };
        let targets = [];

        const diffSpecs = {
            1: { radiusBonus: 1.3, speedBonus: 0.5, desc: "<strong>🟢 레벨 1 사양:</strong><br>과녁 반경: 기본 1.3배 확대<br>이동 속도: 0.5배 감속" },
            2: { radiusBonus: 1.0, speedBonus: 1.0, desc: "<strong>🟡 레벨 2 사양:</strong><br>과녁 반경: 표준 실전 규격<br>이동 속도: 1.0배 표준 속도" },
            3: { radiusBonus: 0.7, speedBonus: 1.5, desc: "<strong>🟠 레벨 3 사양:</strong><br>과녁 반경: 30% 압축 축소<br>이동 속도: 1.5배 고속 난선형 무빙" },
            4: { radiusBonus: 0.4, speedBonus: 2.3, desc: "<strong>🔴 레벨 4 사양:</strong><br>과녁 반경: 초미세 픽셀 크기<br>이동 속도: 2.3배 하이퍼 소닉 무빙" }
        };

        // ⚙️ 포인터 잠금 없이 창 전체에서 마우스 움직임(델타 값)만 추적하는 우회 엔진
        window.addEventListener('mousemove', (e) => {
            // 마우스 가속도나 윈도우 해상도 좌표 한계를 무시하기 위해 무조건 movementX/Y 값을 추적합니다.
            let movementX = e.movementX;
            let movementY = e.movementY;

            // 브라우저 환경에 따라 movementX가 지원되지 않는 구형 예외 처리 보정
            if (movementX === undefined) {
                if (lastRealX !== null) {
                    movementX = e.clientX - lastRealX;
                    movementY = e.clientY - lastRealY;
                } else {
                    movementX = 0;
                    movementY = 0;
                }
            }

            lastRealX = e.clientX;
            lastRealY = e.clientY;

            // 게임 진행 여부 상관없이 마우스 이동 변화량에 감도를 곱해 고유 조준선 좌표 업데이트
            // 0.65 상수를 통해 발로란트/오버워치 표준 감도 배율 체감 링크를 부드럽게 조정
            mouseX += movementX * sensitivity * 0.65;
            mouseY += movementY * sensitivity * 0.65;

            // 조준선이 가상 패널 밖으로 튀어나가지 않도록 마진 차단
            mouseX = Math.max(0, Math.min(canvas.width, mouseX));
            mouseY = Math.max(0, Math.min(canvas.height, mouseY));
        });

        function loadSavedScores() {
            if (localStorage.getItem('aimlab_diff_bypass_hs')) {
                highScores = JSON.parse(localStorage.getItem('aimlab_diff_bypass_hs'));
            }
            if (localStorage.getItem('aimlab_saved_bypass_sens')) {
                sensitivity = parseFloat(localStorage.getItem('aimlab_saved_bypass_sens'));
                document.getElementById('sens-slider').value = sensitivity;
                document.getElementById('sens-val').innerText = sensitivity.toFixed(2);
            }
            renderScoresUI();
        }

        function saveScores() {
            localStorage.setItem('aimlab_diff_bypass_hs', JSON.stringify(highScores));
        }

        function updateSensitivity(val) {
            sensitivity = parseFloat(val);
            document.getElementById('sens-val').innerText = sensitivity.toFixed(2);
            localStorage.setItem('aimlab_saved_bypass_sens', sensitivity);
        }

        function renderScoresUI() {
            document.getElementById('record-board').innerHTML = `
                <div style="display:flex; justify-content:space-between; color:#6b7280; border-bottom:1px solid #1f2937; padding-bottom:4px;">
                    <span>MODE</span><span>PERSONAL BEST</span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-top:4px;">
                    <span>🎯 GRIDSHOT</span><span style="color:#38bdf8; font-weight:bold;">${highScores.gridshot}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span>🔄 TRACKING</span><span style="color:#a855f7; font-weight:bold;">${highScores.tracking}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span>⚡ MICROFLEX</span><span style="color:#f43f5e; font-weight:bold;">${highScores.microflex}</span>
                </div>
            `;
        }

        function clearAllData() {
            highScores = { gridshot: 0, tracking: 0, microflex: 0 };
            saveScores(); renderScoresUI();
        }

        function setDifficulty(lvl) {
            if (isPlaying) return;
            difficulty = lvl;
            const colorMap = { 1: '#22c55e', 2: '#eab308', 3: '#f97316', 4: '#ef4444' };
            for(let i=1; i<=4; i++) {
                const btn = document.getElementById('df-' + i);
                if (i === lvl) {
                    btn.style.background = colorMap[lvl]; btn.style.color = 'black'; btn.style.border = 'none';
                } else {
                    btn.style.background = '#07080b'; btn.style.color = '#e5e7eb'; btn.style.border = '1px solid #374151';
                }
            }
            document.getElementById('df-desc').innerHTML = diffSpecs[lvl].desc;
            initTargets();
        }

        function changeMode(m) {
            if (isPlaying) return;
            mode = m;
            ['grid', 'track', 'micro'].forEach(k => {
                const el = document.getElementById('m-' + k);
                if (k === m.substring(0,5)) {
                    el.style.background = '#00f2fe'; el.style.color = 'black';
                } else {
                    el.style.background = '#07080b'; el.style.color = '#00f2fe';
                }
            });
            initTargets();
        }

        function initTargets() {
            targets = [];
            if (mode === 'gridshot') {
                for(let i=0; i<3; i++) targets.push(generateTargetData());
            } else {
                targets.push(generateTargetData());
            }
        }

        function generateTargetData() {
            let baseRadius = 18;
            let baseSpeed = 5;

            if (mode === 'microflex') {
                baseRadius = 7; baseSpeed = 7.5;
            } else if (mode === 'tracking') {
                baseRadius = 22; baseSpeed = 5.5;
            }

            let spec = diffSpecs[difficulty];
            let finalRadius = baseRadius * spec.radiusBonus;
            let finalSpeed = baseSpeed * spec.speedBonus;

            return {
                x: 60 + Math.random() * (canvas.width - 120),
                y: 60 + Math.random() * (canvas.height - 120),
                radius: finalRadius,
                vx: (Math.random() - 0.5) * finalSpeed,
                vy: (Math.random() - 0.5) * finalSpeed
            };
        }

        function startSession() {
            if (isPlaying) return;
            isPlaying = true;
            score = 0; timeLeft = 30.0; totalShots = 0; hitShots = 0;
            initTargets();
            document.getElementById('start-btn').style.background = '#4b5563';
            document.getElementById('start-btn').innerText = "⏱ FOCUS LIVE";
        }

        function endSession() {
            isPlaying = false;
            document.getElementById('start-btn').style.background = '#34d399';
            document.getElementById('start-btn').innerText = "▶ 훈련 시작";

            if (score > highScores[mode]) {
                highScores[mode] = score;
                saveScores();
                renderScoresUI();
            }
        }

        // 마우스 클릭 시 가상 조준선 좌표(mouseX, mouseY) 기준으로 히트박스 판정
        canvas.addEventListener('mousedown', () => {
            if (!isPlaying) return;
            totalShots++;
            let hitAny = false;

            for (let i = 0; i < targets.length; i++) {
                let dist = Math.hypot(mouseX - targets[i].x, mouseY - targets[i].y);
                if (dist <= targets[i].radius) {
                    hitShots++;
                    score += 100;
                    hitAny = true;
                    if (mode === 'gridshot' || mode === 'microflex') {
                        targets[i] = generateTargetData();
                    }
                    break;
                }
            }
            if (!hitAny && mode !== 'tracking') score = Math.max(0, score - 20);
            updateDashboard();
        });

        function updateDashboard() {
            document.getElementById('ui-score').innerText = "SCORE: " + score;
            let acc = totalShots > 0 ? Math.round((hitShots / totalShots) * 100) : 100;
            document.getElementById('ui-acc').innerText = "ACC: " + acc + "%";
            document.getElementById('ui-time').innerText = "TIME: " + timeLeft.toFixed(1) + "s";
        }

        function loop() {
            ctx.fillStyle = '#090b11'; ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.strokeStyle = '#121620'; ctx.lineWidth = 1;
            for(let i=0; i<canvas.width; i+=50) { ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,canvas.height); ctx.stroke(); }
            for(let j=0; j<canvas.height; j+=50) { ctx.beginPath(); ctx.moveTo(0,j); ctx.lineTo(canvas.width,j); ctx.stroke(); }

            if (isPlaying) {
                timeLeft -= 1/60;
                if (timeLeft <= 0) { timeLeft = 0; endSession(); }
                updateDashboard();

                targets.forEach((t) => {
                    if (mode === 'tracking' || mode === 'microflex') {
                        t.x += t.vx; t.y += t.vy;
                        if(t.x - t.radius < 0 || t.x + t.radius > canvas.width) t.vx *= -1;
                        if(t.y - t.radius < 0 || t.y + t.radius > canvas.height) t.vy *= -1;

                        if (mode === 'tracking') {
                            let dist = Math.hypot(mouseX - t.x, mouseY - t.y);
                            if (dist <= t.radius) score += 3;
                        }
                    }

                    ctx.save();
                    if(mode === 'gridshot') ctx.strokeStyle = '#38bdf8';
                    else if(mode === 'tracking') ctx.strokeStyle = '#a855f7';
                    else ctx.strokeStyle = '#f43f5e';
                    
                    ctx.lineWidth = 2.5;
                    ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI*2); ctx.stroke();
                    ctx.restore();
                });
            } else {
                ctx.fillStyle = 'rgba(255,255,255,0.25)'; ctx.font = '14px sans-serif'; ctx.textAlign = 'center';
                ctx.fillText("감도와 난이도 레벨(레벨 1~4)을 맞추고 상단 [▶ 훈련 시작]을 누르세요.", canvas.width/2, canvas.height/2);
            }

            // 🛠️ 보안 우회형 고정식 '빨간색 점(Red Dot)' 조준선 렌더링 Engine
            ctx.save();
            ctx.fillStyle = '#FF0000';
            ctx.beginPath();
            ctx.arc(mouseX, mouseY, 3.0, 0, Math.PI * 2); // 직관성을 위해 가시성 소폭 상향(3px)
            ctx.fill();
            ctx.restore();

            requestAnimationFrame(loop);
        }

        loadSavedScores();
        initTargets();
        loop();
    </script>
    """
    st.components.v1.html(html_src, height=590)

if __name__ == "__main__":
    main()
