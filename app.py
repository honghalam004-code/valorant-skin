import streamlit as st

def main():
    st.set_page_config(page_title="AIMLAB: REAL TRUCKING ENGINE", layout="wide")

    st.markdown("""
        <style>
        .main { background-color: #07080b; color: #e5e7eb; font-family: 'Segoe UI', monospace; }
        .stButton > button {
            background: linear-gradient(135deg, #a855f7, #c084fc) !important;
            color: white !important; font-weight: bold !important; border: none !important;
            padding: 12px; border-radius: 4px; width: 100%; letter-spacing: 1px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center; color:#a855f7; font-weight:900;'>🎯 AIMLAB: ADVANCED TRACKING EDITION</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#4b5563; font-size:14px;'>불규칙 관성 AI 트래킹 시스템 | 브레이킹-유지력 연동 판정 | 그리드샷/마이크로플렉스 버그 완벽 수정</p>", unsafe_allow_html=True)

    html_src = """
    <div style="max-width:1240px; margin:0 auto; display:flex; gap:20px; justify-content:center;">
        
        <div style="flex: 1; text-align:center;">
            <div style="display:flex; justify-content:space-between; align-items:center; background:#111827; padding:12px 20px; border-radius:6px; margin-bottom:12px; border:1px solid #1f2937;">
                <div style="display:flex; gap:6px;">
                    <button onclick="changeMode('gridshot')" id="m-grid" style="background:#07080b; color:#00f2fe; border:1px solid #00f2fe; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">🎯 GRIDSHOT</button>
                    <button onclick="changeMode('tracking')" id="m-track" style="background:#a855f7; color:white; border:none; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">🔄 VAL-TRACKING</button>
                    <button onclick="changeMode('microflex')" id="m-micro" style="background:#07080b; color:#00f2fe; border:1px solid #00f2fe; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">⚡ MICROFLEX</button>
                    <button onclick="changeMode('breaking')" id="m-break" style="background:#07080b; color:#ff4655; border:1px solid #ff4655; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">⚡ VAL-BREAKING</button>
                </div>
                <div style="display:flex; gap:15px; font-family:monospace; font-size:15px; font-weight:bold; align-items:center;">
                    <div style="color:#00f2fe;" id="ui-score">SCORE: 0</div>
                    <div style="color:#34d399;" id="ui-acc">ACC: 100%</div>
                    <div style="color:#f87171;" id="ui-time">TIME: 30.0s</div>
                </div>
                
                <div style="display:flex; gap:6px;">
                    <button onclick="togglePause()" id="pause-btn" style="background:#eab308; color:black; border:none; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; display:none;">⏸ 정지</button>
                    <button onclick="startSession()" id="start-btn" style="background:#34d399; color:black; border:none; padding:8px 18px; font-weight:bold; cursor:pointer; border-radius:4px;">▶ 훈련 시작</button>
                </div>
            </div>
            
            <div style="position:relative;">
                <canvas id="aimCanvas" width="860" height="510" style="background:#090b11; border:2px solid #1f2937; border-radius:6px; cursor:none;"></canvas>
            </div>
        </div>

        <div style="width:280px; display:flex; flex-direction:column; gap:15px; text-align:left;">
            
            <div style="background:#111827; padding:16px; border-radius:6px; border:1px solid #1f2937;">
                <div style="color:#a855f7; font-size:12px; font-weight:bold; letter-spacing:1px; margin-bottom:8px;">⚙️ REAL FPS SENSITIVITY</div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <span style="font-size:13px; color:#9ca3af;">조준선 감도 배율</span>
                    <span style="font-size:16px; font-weight:bold; color:#a855f7; font-family:monospace;" id="sens-val">1.00</span>
                </div>
                <input type="range" id="sens-slider" min="0.1" max="4.0" step="0.05" value="1.0" oninput="updateSensitivity(this.value)" style="width:100%; accent-color:#a855f7; cursor:pointer;">
                <div style="font-size:11px; color:#6b7280; margin-top:6px; line-height:1.4;">* VAL-TRACKING 모드는 마우스 클릭을 유지한 상태로 표적을 따라가야 스코어가 축적됩니다. [P] 일시정지 가능.</div>
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

        // 메인 데이터 메커니즘
        let mode = 'tracking'; // 기본을 트래킹으로 세팅
        let difficulty = 1;
        let sensitivity = 1.0;
        let isPlaying = false;
        let isPaused = false;
        let score = 0;
        let timeLeft = 30.0;
        let totalShots = 0;
        let hitShots = 0;

        // 조준선 좌표
        let mouseX = 430, mouseY = 255;
        let rawMouseX = 430, rawMouseY = 255;
        let isMouseDown = false; // 트래킹 마우스 누름 감지용

        // 플레이어 무빙 물리
        let playerX = 430;
        let playerVx = 0;
        const playerMaxSpeed = 5.5;
        const playerAcc = 0.8;
        const playerFric = 0.5;
        let keys = { a: false, d: false };
        let showMovingError = false;
        let errorTimer = 0;

        let highScores = { gridshot: 0, tracking: 0, microflex: 0, breaking: 0 };
        let targets = [];

        const diffSpecs = {
            1: { radiusBonus: 1.3, speedBonus: 0.5, desc: "<strong>🟢 레벨 1 사양:</strong><br>과녁 반경: 기본 1.3배 확대<br>이동 속도: 0.5배 감속" },
            2: { radiusBonus: 1.0, speedBonus: 1.0, desc: "<strong>🟡 레벨 2 사양:</strong><br>과녁 반경: 표준 실전 규격<br>이동 속도: 1.0배 표준 속도" },
            3: { radiusBonus: 0.7, speedBonus: 1.5, desc: "<strong>🟠 레벨 3 사양:</strong><br>과녁 반경: 30% 압축 축소<br>이동 속도: 1.5배 고속 무빙" },
            4: { radiusBonus: 0.4, speedBonus: 2.3, desc: "<strong>🔴 레벨 4 사양:</strong><br>과녁 반경: 초미세 픽셀 크기<br>이동 속도: 2.3배 초고속 무빙" }
        };

        window.addEventListener('keydown', (e) => {
            if (e.key.toLowerCase() === 'a') keys.a = true;
            if (e.key.toLowerCase() === 'd') keys.d = true;
            if (e.key.toLowerCase() === 'p') { togglePause(); }
        });

        window.addEventListener('keyup', (e) => {
            if (e.key.toLowerCase() === 'a') keys.a = false;
            if (e.key.toLowerCase() === 'd') keys.d = false;
        });

        canvas.addEventListener('mousemove', (e) => {
            let rect = canvas.getBoundingClientRect();
            rawMouseX = e.clientX - rect.left;
            rawMouseY = e.clientY - rect.top;
        });

        canvas.addEventListener('mousedown', () => { isMouseDown = true; });
        window.addEventListener('mouseup', () => { isMouseDown = false; });

        function togglePause() {
            if (!isPlaying) return;
            isPaused = !isPaused;
            const pauseBtn = document.getElementById('pause-btn');
            if (isPaused) {
                pauseBtn.innerText = "▶ 재개"; pauseBtn.style.background = "#34d399";
            } else {
                pauseBtn.innerText = "⏸ 정지"; pauseBtn.style.background = "#eab308";
            }
        }

        function loadSavedScores() {
            if (localStorage.getItem('aimlab_v4_perfect_hs')) {
                highScores = JSON.parse(localStorage.getItem('aimlab_v4_perfect_hs'));
            }
            if (localStorage.getItem('aimlab_v4_perfect_sens')) {
                sensitivity = parseFloat(localStorage.getItem('aimlab_v4_perfect_sens'));
                document.getElementById('sens-slider').value = sensitivity;
                document.getElementById('sens-val').innerText = sensitivity.toFixed(2);
            }
            renderScoresUI();
        }

        function saveScores() {
            localStorage.setItem('aimlab_v4_perfect_hs', JSON.stringify(highScores));
        }

        function updateSensitivity(val) {
            sensitivity = parseFloat(val);
            document.getElementById('sens-val').innerText = sensitivity.toFixed(2);
            localStorage.setItem('aimlab_v4_perfect_sens', sensitivity);
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
                    <span>🔄 VAL-TRACKING</span><span style="color:#a855f7; font-weight:bold;">${highScores.tracking}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span>⚡ MICROFLEX</span><span style="color:#f43f5e; font-weight:bold;">${highScores.microflex}</span>
                </div>
                <div style="display:flex; justify-content:space-between; border-top:1px dashed #374151; pt:4px; margin-top:4px;">
                    <span>⚡ BREAKING</span><span style="color:#ff4655; font-weight:bold;">${highScores.breaking}</span>
                </div>
            `;
        }

        function clearAllData() {
            highScores = { gridshot: 0, tracking: 0, microflex: 0, breaking: 0 };
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
            ['grid', 'track', 'micro', 'break'].forEach(k => {
                const el = document.getElementById('m-' + k);
                let targetKey = m.substring(0,5);
                if (m === 'breaking') targetKey = 'break';
                
                if (k === targetKey) {
                    el.style.background = m === 'breaking' ? '#ff4655' : (m === 'tracking' ? '#a855f7' : '#00f2fe');
                    el.style.color = 'white'; el.style.border = 'none';
                } else {
                    el.style.background = '#07080b';
                    el.style.color = k === 'break' ? '#ff4655' : (k === 'track' ? '#a855f7' : '#00f2fe');
                    el.style.border = '1px solid currentColor';
                }
            });
            initTargets();
        }

        function initTargets() {
            targets = [];
            let count = (mode === 'gridshot') ? 3 : 1;
            for(let i=0; i<count; i++) {
                targets.push(generateTargetData());
            }
        }

        function generateTargetData() {
            let baseRadius = 18; let baseSpeed = 4.0;
            if (mode === 'microflex') { baseRadius = 7; baseSpeed = 7.0; }
            else if (mode === 'tracking') { baseRadius = 20; baseSpeed = 4.5; } // 트래킹 전용 속도 세팅
            else if (mode === 'breaking') { baseRadius = 15; baseSpeed = 3.5; }

            let spec = diffSpecs[difficulty];
            let finalRadius = baseRadius * spec.radiusBonus;
            let finalSpeed = baseSpeed * spec.speedBonus;

            // 트래킹 모드 전용 AI 관성 변화 축적기 구조 정의
            return {
                x: 80 + Math.random() * (canvas.width - 160),
                y: 80 + Math.random() * ((mode === 'breaking' || mode === 'tracking') ? 140 : (canvas.height - 160)),
                radius: finalRadius,
                vx: (Math.random() > 0.5 ? 1 : -1) * finalSpeed,
                vy: (mode === 'breaking' || mode === 'tracking') ? 0 : (Math.random() - 0.5) * finalSpeed,
                maxSpeed: finalSpeed,
                changeTimer: Math.floor(Math.random() * 40) + 30 // 불규칙 방향 전환 타이머 프레임
            };
        }

        function startSession() {
            if (isPlaying) return;
            isPlaying = true; isPaused = false;
            score = 0; timeLeft = 30.0; totalShots = 0; hitShots = 0;
            playerX = 430; playerVx = 0;
            initTargets();
            document.getElementById('start-btn').style.background = '#4b5563';
            document.getElementById('start-btn').innerText = "⏱ FOCUS LIVE";
            document.getElementById('pause-btn').style.display = "inline-block";
        }

        function endSession() {
            isPlaying = false; isPaused = false;
            document.getElementById('start-btn').style.background = '#34d399';
            document.getElementById('start-btn').innerText = "▶ 훈련 시작";
            document.getElementById('pause-btn').style.display = "none";

            if (score > highScores[mode]) {
                highScores[mode] = score; saveScores(); renderScoresUI();
            }
        }

        // 클릭 슈팅 판정 (클릭식 모드 대응)
        canvas.addEventListener('mousedown', () => {
            if (!isPlaying || isPaused) return;
            if (mode === 'tracking') return; // 트래킹 모드는 누르고 있는 유지력 판정이라 하단 루프에서 별도 처리

            totalShots++;
            let hitAny = false;
            for (let i = 0; i < targets.length; i++) {
                let dist = Math.hypot(mouseX - targets[i].x, mouseY - targets[i].y);
                if (dist <= targets[i].radius) {
                    if (mode === 'breaking' && Math.abs(playerVx) > 0.2) {
                        score = Math.max(0, score - 40);
                        showMovingError = true; errorTimer = 25;
                        updateDashboard(); return;
                    }
                    hitShots++; score += 100; hitAny = true;
                    targets[i] = generateTargetData(); break;
                }
            }
            if (!hitAny) score = Math.max(0, score - 20);
            updateDashboard();
        });

        function updateDashboard() {
            document.getElementById('ui-score').innerText = "SCORE: " + score;
            let acc = totalShots > 0 ? Math.round((hitShots / totalShots) * 100) : 100;
            if (mode === 'tracking') acc = 100; // 트래킹 모드는 정확도 연산 열외
            document.getElementById('ui-acc').innerText = "ACC: " + acc + "%";
            document.getElementById('ui-time').innerText = "TIME: " + timeLeft.toFixed(1) + "s";
        }

        function loop() {
            if (isPlaying && isPaused) { requestAnimationFrame(loop); return; }

            ctx.fillStyle = '#090b11'; ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 백그라운드 그리드 드로잉
            ctx.strokeStyle = '#121620'; ctx.lineWidth = 1;
            for(let i=0; i<canvas.width; i+=50) { ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,canvas.height); ctx.stroke(); }
            for(let j=0; j<canvas.height; j+=50) { ctx.beginPath(); ctx.moveTo(0,j); ctx.lineTo(canvas.width,j); ctx.stroke(); }

            // 플레이어 좌우 무빙 물리
            if (keys.a) playerVx = Math.max(-playerMaxSpeed, playerVx - playerAcc);
            else if (keys.d) playerVx = Math.min(playerMaxSpeed, playerVx + playerAcc);
            else {
                if (playerVx > 0) playerVx = Math.max(0, playerVx - playerFric);
                else if (playerVx < 0) playerVx = Math.min(0, playerVx + playerFric);
            }
            playerX = Math.max(40, Math.min(canvas.width - 40, playerX + playerVx));

            // 탄퍼짐 이펙트 알고리즘 (브레이킹 모드 전용)
            let spreadX = 0, spreadY = 0;
            if (mode === 'breaking' && Math.abs(playerVx) > 0.2) {
                spreadX = (Math.random() - 0.5) * (Math.abs(playerVx) * 12);
                spreadY = (Math.random() - 0.5) * (Math.abs(playerVx) * 12);
            }
            mouseX = rawMouseX + spreadX; mouseY = rawMouseY + spreadY;

            if (isPlaying) {
                timeLeft -= 1/60;
                if (timeLeft <= 0) { timeLeft = 0; endSession(); }
                updateDashboard();

                targets.forEach((t) => {
                    // 🔄 VAL-TRACKING 및 BREAKING 모드용 관성 불규칙 AI 이동 제어
                    if (mode === 'tracking' || mode === 'breaking') {
                        t.changeTimer--;
                        if (t.changeTimer <= 0) {
                            // 방향 전환 시 즉시 튕기지 않고 속도를 부드럽게 뒤집음 (엇박자 관성 무빙)
                            t.vx = (Math.random() > 0.5 ? 1 : -1) * t.maxSpeed;
                            t.changeTimer = Math.floor(Math.random() * 50) + 35;
                        }
                    }

                    t.x += t.vx; t.y += t.vy;
                    if(t.x - t.radius < 15 || t.x + t.radius > canvas.width - 15) t.vx *= -1;
                    if(t.y - t.radius < 15 || t.y + t.radius > canvas.height - 15) t.vy *= -1;

                    // 🔄 실전 트래킹 실시간 연속 적중 및 브레이킹 판정 연산 루프
                    if (mode === 'tracking') {
                        let dist = Math.hypot(mouseX - t.x, mouseY - t.y);
                        // 에임이 원 안에 들어가 있고 + 마우스 왼쪽을 누르고 있으며 + 내 기동이 멈춘 상태여야 데미지 누적
                        if (dist <= t.radius && isMouseDown) {
                            if (Math.abs(playerVx) <= 0.2) {
                                score += 2; // 완벽한 무빙 트래킹 가점
                            } else {
                                score += 0; // 무빙샷 중일 땐 트래킹 점수 없음 페널티
                            }
                        }
                    }

                    // 과녁 드로잉
                    ctx.save();
                    if(mode === 'gridshot') ctx.strokeStyle = '#38bdf8';
                    else if(mode === 'tracking') ctx.strokeStyle = '#a855f7'; // 트래킹 퍼플
                    else if(mode === 'microflex') ctx.strokeStyle = '#f43f5e';
                    else ctx.strokeStyle = '#ff4655';
                    
                    ctx.lineWidth = 2.5;
                    ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI*2); ctx.stroke();
                    ctx.restore();
                });
            } else {
                ctx.fillStyle = 'rgba(255,255,255,0.25)'; ctx.font = '14px sans-serif'; ctx.textAlign = 'center';
                ctx.fillText("원하는 모드와 난이도를 세팅하고 상단 [▶ 훈련 시작]을 클릭하세요.", canvas.width/2, canvas.height/2 - 20);
                ctx.fillText("VAL-TRACKING 모드: 마우스 좌클릭을 유지한 상태로 좌우 무빙 AI 과녁을 따라가세요.", canvas.width/2, canvas.height/2 + 10);
            }

            if (showMovingError && errorTimer > 0) {
                ctx.save();
                ctx.fillStyle = '#ff4655'; ctx.font = 'bold 20px sans-serif'; ctx.textAlign = 'center';
                ctx.fillText("❌ 무빙샷 불허 (탄퍼짐 발생!)", canvas.width/2, 70); ctx.restore();
                errorTimer--; if(errorTimer <= 0) showMovingError = false;
            }

            // 하단 플레이어 상태 박스 드로잉
            ctx.save();
            ctx.fillStyle = Math.abs(playerVx) <= 0.2 ? '#22c55e' : '#eab308';
            ctx.fillRect(playerX - 25, canvas.height - 25, 50, 10);
            ctx.fillStyle = '#6b7280'; ctx.font = '11px sans-serif'; ctx.textAlign = 'center';
            ctx.fillText("PLAYER", playerX, canvas.height - 32); ctx.restore();

            // 1:1 조준선 드로잉
            ctx.save();
            ctx.fillStyle = '#FF0000';
            ctx.beginPath(); ctx.arc(mouseX, mouseY, 3.5, 0, Math.PI * 2); ctx.fill();
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
