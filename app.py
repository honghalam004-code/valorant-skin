import streamlit as st

def main():
    st.set_page_config(page_title="FPS AIMLAB RED DOT ENGINE", layout="wide")

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

    st.markdown("<h2 style='text-align:center; color:#00f2fe; font-weight:900;'>🎯 AIMLAB: RED DOT SENSITIVITY ENGINE</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#4b5563; font-size:14px;'>빨간색 점 조준선 | 실시간 마우스 감도 튜닝 | 난이도 레벨 제어 | 무반동 레이저 에임</p>", unsafe_allow_html=True)

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
            
            <canvas id="aimCanvas" width="860" height="510" style="background:#090b11; border:2px solid #1f2937; border-radius:6px; cursor:none;"></canvas>
        </div>

        <div style="width:280px; display:flex; flex-direction:column; gap:15px; text-align:left;">
            
            <div style="background:#111827; padding:16px; border-radius:6px; border:1px solid #1f2937;">
                <div style="color:#34d399; font-size:12px; font-weight:bold; letter-spacing:1px; margin-bottom:8px;">⚙️ MOUSE SENSITIVITY</div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <span style="font-size:13px; color:#9ca3af;">현재 감도 수치</span>
                    <span style="font-size:16px; font-weight:bold; color:#34d399; font-family:monospace;" id="sens-val">1.0</span>
                </div>
                <input type="range" id="sens-slider" min="0.1" max="5.0" step="0.1" value="1.0" oninput="updateSensitivity(this.value)" style="width:100%; accent-color:#34d399; cursor:pointer;">
                <div style="font-size:11px; color:#6b7280; margin-top:6px; line-height:1.3;">* 인게임 마우스 속도를 배율로 조절합니다. 본인 신체 밸런스에 맞게 설정하세요.</div>
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

        // 조준선 좌표 제어 변수
        let mouseX = 430, mouseY = 255;
        let realX = 430, realY = 255;

        let highScores = { gridshot: 0, tracking: 0, microflex: 0 };
        let targets = [];

        const diffSpecs = {
            1: { radiusBonus: 1.3, speedBonus: 0.5, desc: "<strong>🟢 레벨 1 사양:</strong><br>과녁 반경: 기본 1.3배 확대<br>이동 속도: 0.5배 감속 (기초 훈련)" },
            2: { radiusBonus: 1.0, speedBonus: 1.0, desc: "<strong>🟡 레벨 2 사양:</strong><br>과녁 반경: 표준 실전 규격<br>이동 속도: 1.0배 표준 속도 기동" },
            3: { radiusBonus: 0.7, speedBonus: 1.5, desc: "<strong>🟠 레벨 3 사양:</strong><br>과녁 반경: 30% 압축 축소<br>이동 속도: 1.5배 고속 난선형 무빙" },
            4: { radiusBonus: 0.4, speedBonus: 2.3, desc: "<strong>🔴 레벨 4 사양:</strong><br>과녁 반경: 초미세 픽셀 크기<br>이동 속도: 2.3배 하이퍼 소닉 무빙" }
        };

        function loadSavedScores() {
            if (localStorage.getItem('aimlab_diff_sens_v6')) {
                highScores = JSON.parse(localStorage.getItem('aimlab_diff_sens_v6'));
            }
            if (localStorage.getItem('aimlab_saved_sens')) {
                sensitivity = parseFloat(localStorage.getItem('aimlab_saved_sens'));
                document.getElementById('sens-slider').value = sensitivity;
                document.getElementById('sens-val').innerText = sensitivity.toFixed(1);
            }
            renderScoresUI();
        }

        function saveScores() {
            localStorage.setItem('aimlab_diff_sens_v6', JSON.stringify(highScores));
        }

        function updateSensitivity(val) {
            sensitivity = parseFloat(val);
            document.getElementById('sens-val').innerText = sensitivity.toFixed(1);
            localStorage.setItem('aimlab_saved_sens', sensitivity);
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

        canvas.addEventListener('mousemove', (e) => {
            let rect = canvas.getBoundingClientRect();
            let targetX = (e.clientX - rect.left) * (canvas.width / rect.width);
            let targetY = (e.clientY - rect.top) * (canvas.height / rect.height);

            let deltaX = targetX - realX;
            let deltaY = targetY - realY;

            mouseX = Math.max(0, Math.min(canvas.width, mouseX + deltaX * sensitivity));
            mouseY = Math.max(0, Math.min(canvas.height, mouseY + deltaY * sensitivity));

            realX = targetX;
            realY = targetY;
        });

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
                ctx.fillText("우측에서 감도와 난이도(레벨)를 세팅하고 [▶ 훈련 시작]을 누르세요.", canvas.width/2, canvas.height/2);
            }

            // 🛠️ 핵심 변경 사항: 완전 무반동 고정식 '빨간색 점(Red Dot)' 조준선 렌더링 Engine
            ctx.save();
            ctx.fillStyle = '#FF0000'; // 선명한 핫 레드 컬러 고정
            ctx.beginPath();
            ctx.arc(mouseX, mouseY, 2.5, 0, Math.PI * 2); // 반경 2.5px의 깔끔한 점 형태
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
