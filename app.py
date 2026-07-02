import streamlit as st

def main():
    st.set_page_config(page_title="AIMLAB: ULTIMATE REBOOT", layout="wide")

    st.markdown("""
        <style>
        .main { background-color: #07080b; color: #e5e7eb; font-family: 'Segoe UI', monospace; }
        .stButton > button {
            background: linear-gradient(135deg, #ff4655, #ff7682) !important;
            color: white !important; font-weight: bold !important; border: none !important;
            padding: 12px; border-radius: 4px; width: 100%; letter-spacing: 1px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center; color:#ff4655; font-weight:900;'>🎯 AIMLAB: ULTIMATE REBOOT V2</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#4b5563; font-size:14px;'>트래킹 정상화 | 2라이프 데스 시스템 | 킬사운드 탑재 | 훈련 탈출 시스템</p>", unsafe_allow_html=True)

    html_src = """
    <div style="max-width:1240px; margin:0 auto; display:flex; gap:20px; justify-content:center;">
        
        <div style="flex: 1; text-align:center;">
            <div style="display:flex; justify-content:space-between; align-items:center; background:#111827; padding:12px 20px; border-radius:6px; margin-bottom:12px; border:1px solid #1f2937;">
                <div style="display:flex; gap:6px;">
                    <button onclick="changeMode('gridshot')" id="m-grid" style="background:#07080b; color:#00f2fe; border:1px solid #00f2fe; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">🎯 GRIDSHOT</button>
                    <button onclick="changeMode('tracking')" id="m-track" style="background:#07080b; color:#00f2fe; border:1px solid #00f2fe; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">🔄 TRACKING</button>
                    <button onclick="changeMode('microflex')" id="m-micro" style="background:#07080b; color:#00f2fe; border:1px solid #00f2fe; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">⚡ MICROFLEX</button>
                    <button onclick="changeMode('breaking')" id="m-break" style="background:#ff4655; color:white; border:none; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">⚡ VAL-BREAKING</button>
                </div>
                <div style="display:flex; gap:15px; font-family:monospace; font-size:15px; font-weight:bold; align-items:center;">
                    <div style="color:#00f2fe;" id="ui-score">SCORE: 0</div>
                    <div style="color:#34d399;" id="ui-acc">ACC: 100%</div>
                    <div style="color:#f87171;" id="ui-time">TIME: 30.0s</div>
                </div>
                
                <div style="display:flex; gap:6px;">
                    <button onclick="quitSession()" id="quit-btn" style="background:#ef4444; color:white; border:none; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; display:none;">🚪 훈련 나가기</button>
                    <button onclick="startSession()" id="start-btn" style="background:#34d399; color:black; border:none; padding:8px 18px; font-weight:bold; cursor:pointer; border-radius:4px;">▶ 훈련 시작</button>
                </div>
            </div>
            
            <div style="position:relative;">
                <canvas id="aimCanvas" width="860" height="510" style="background:#090b11; border:2px solid #1f2937; border-radius:6px; cursor:none;"></canvas>
            </div>
        </div>

        <div style="width:280px; display:flex; flex-direction:column; gap:15px; text-align:left;">
            
            <div style="background:#111827; padding:16px; border-radius:6px; border:1px solid #1f2937;">
                <div style="color:#ff4655; font-size:12px; font-weight:bold; letter-spacing:1px; margin-bottom:8px;">⚙️ REAL FPS SENSITIVITY</div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <span style="font-size:13px; color:#9ca3af;">조준선 감도 배율</span>
                    <span style="font-size:16px; font-weight:bold; color:#ff4655; font-family:monospace;" id="sens-val">1.00</span>
                </div>
                <input type="range" id="sens-slider" min="0.1" max="4.0" step="0.05" value="1.0" oninput="updateSensitivity(this.value)" style="width:100%; accent-color:#ff4655; cursor:pointer;">
                <div style="font-size:11px; color:#6b7280; margin-top:6px; line-height:1.4;">* 💡 <b>트래킹 모드:</b> 이제 표적이 정상 구동하며 마우스를 누르고 있으면 점수가 실시간 상승합니다.</div>
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
                    <strong>🟢 레벨 1 사양:</strong><br>과녁 반경: 1.4배 상향<br>투사체 속도: 느림
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

        // 웹 오디오 API를 활용한 즉시 반응형 킬사운드 생성기
        let audioCtx = null;
        function playKillSound() {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                
                let osc = audioCtx.createOscillator();
                let gain = audioCtx.createGain();
                
                osc.type = 'triangle'; 
                osc.frequency.setValueAtTime(587.33, audioCtx.currentTime); // D5 노출
                osc.frequency.exponentialRampToValueAtTime(880.00, audioCtx.currentTime + 0.04); // A5 플릭 사운드 변조
                
                gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.12);
                
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.12);
            } catch(e) {}
        }

        let mode = 'breaking'; 
        let difficulty = 1;
        let sensitivity = 1.0;
        let isPlaying = false;
        let score = 0;
        let timeLeft = 30.0;
        let totalShots = 0;
        let hitShots = 0;

        // VAL-BREAKING 전용 생명력 시스템 (2번 맞으면 게임오버)
        let playerLives = 2;

        let mouseX = 430, mouseY = 255;
        let rawMouseX = 430, rawMouseY = 255;
        let isMouseDown = false;

        let playerX = 430;
        let playerVx = 0;
        const playerMaxSpeed = 6.0;
        const playerAcc = 0.9;
        const playerFric = 0.55;
        let keys = { a: false, d: false };
        let showMovingError = false;
        let errorTimer = 0;

        let projectiles = [];
        let enemyShootTimer = 0;
        let showHitEffect = false;
        let hitEffectTimer = 0;

        let highScores = { gridshot: 0, tracking: 0, microflex: 0, breaking: 0 };
        let targets = [];

        const diffSpecs = {
            1: { radiusBonus: 1.4, speedBonus: 0.6, projectileSpeed: 2.5, desc: "<strong>🟢 레벨 1 사양:</strong><br>과녁 반경: 1.4배 상향<br>투사체 속도: 느림" },
            2: { radiusBonus: 1.1, speedBonus: 1.1, projectileSpeed: 4.0, desc: "<strong>🟡 레벨 2 사양:</strong><br>과녁 반경: 실전 입문 규격<br>투사체 속도: 보통" },
            3: { radiusBonus: 0.9, speedBonus: 1.6, projectileSpeed: 5.5, desc: "<strong>🟠 레벨 3 사양:</strong><br>과녁 반경: 10% 축소 정밀전<br>투사체 속도: 빠름" },
            4: { radiusBonus: 0.75, speedBonus: 2.2, projectileSpeed: 7.0, desc: "<strong>🔴 레벨 4 사양 (밸런스 패치):</strong><br>과녁 반경: 현실적인 마이크로 타겟팅 (0.75배)<br>투사체 속도: 극속 대응 훈련" }
        };

        window.addEventListener('keydown', (e) => {
            if (e.key.toLowerCase() === 'a') keys.a = true;
            if (e.key.toLowerCase() === 'd') keys.d = true;
        });

        window.addEventListener('keyup', (e) => {
            if (e.key.toLowerCase() === 'a') keys.a = false;
            if (e.key.toLowerCase() === 'd') keys.d = false;
        });

        canvas.addEventListener('mousemove', (e) => {
            if (!isPlaying) return;
            let rect = canvas.getBoundingClientRect();
            rawMouseX = e.clientX - rect.left;
            rawMouseY = e.clientY - rect.top;
        });

        canvas.addEventListener('mousedown', () => { isMouseDown = true; });
        window.addEventListener('mouseup', () => { isMouseDown = false; });

        function loadSavedScores() {
            if (localStorage.getItem('aimlab_v8_hs')) {
                highScores = JSON.parse(localStorage.getItem('aimlab_v8_hs'));
            }
            if (localStorage.getItem('aimlab_v8_sens')) {
                sensitivity = parseFloat(localStorage.getItem('aimlab_v8_sens'));
                document.getElementById('sens-slider').value = sensitivity;
                document.getElementById('sens-val').innerText = sensitivity.toFixed(2);
            }
            renderScoresUI();
        }

        function saveScores() { localStorage.setItem('aimlab_v8_hs', JSON.stringify(highScores)); }

        function updateSensitivity(val) {
            sensitivity = parseFloat(val);
            document.getElementById('sens-val').innerText = sensitivity.toFixed(2);
            localStorage.setItem('aimlab_v8_sens', sensitivity);
        }

        function renderScoresUI() {
            document.getElementById('record-board').innerHTML = `
                <div style="display:flex; justify-content:space-between; color:#6b7280; border-bottom:1px solid #1f2937; padding-bottom:4px;">
                    <span>MODE</span><span>PERSONAL BEST</span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-top:4px;">
                    <span>🎯 GRIDSHOT</span><span style="color:#38bdf8; font-weight:bold;">${highScores.gridshot || 0}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span>🔄 TRACKING</span><span style="color:#00f2fe; font-weight:bold;">${highScores.tracking || 0}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span>⚡ MICROFLEX</span><span style="color:#f43f5e; font-weight:bold;">${highScores.microflex || 0}</span>
                </div>
                <div style="display:flex; justify-content:space-between; border-top:1px dashed #ff4655; padding-top:6px; margin-top:4px;">
                    <span>💥 VAL-BREAKING</span><span style="color:#ff4655; font-weight:bold;">${highScores.breaking || 0}</span>
                </div>
            `;
        }

        function clearAllData() { highScores = { gridshot: 0, tracking: 0, microflex: 0, breaking: 0 }; saveScores(); renderScoresUI(); }

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
            mode = m;
            ['grid', 'track', 'micro', 'break'].forEach(k => {
                const el = document.getElementById('m-' + k);
                let targetKey = m.substring(0,5);
                if (m === 'breaking') targetKey = 'break';
                
                if (k === targetKey) {
                    el.style.background = m === 'breaking' ? '#ff4655' : '#00f2fe';
                    el.style.color = 'black'; el.style.border = 'none';
                } else {
                    el.style.background = '#07080b';
                    el.style.color = k === 'break' ? '#ff4655' : '#00f2fe';
                    el.style.border = '1px solid currentColor';
                }
            });

            if (isPlaying) { quitSession(); }
            initTargets();
            updateDashboard();
        }

        function initTargets() {
            targets = []; projectiles = [];
            let count = (mode === 'gridshot') ? 3 : 1;
            for(let i=0; i<count; i++) targets.push(generateTargetData());
        }

        function generateTargetData() {
            let baseRadius = 18; let baseSpeed = 3.5;
            // 트래킹 모드 전용 표적 물리 속도 정상 부여 완료
            if (mode === 'tracking') { baseRadius = 22; baseSpeed = 4.5; }
            else if (mode === 'microflex') { baseRadius = 16; baseSpeed = 4.0; } 
            else if (mode === 'breaking') { baseRadius = 18; baseSpeed = 2.0; } // 좌우로만 살짝 움직임

            let spec = diffSpecs[difficulty];
            return {
                x: 120 + Math.random() * (canvas.width - 240),
                y: 100 + Math.random() * (mode === 'breaking' ? 80 : (canvas.height - 240)),
                radius: baseRadius * spec.radiusBonus,
                vx: (Math.random() > 0.5 ? 1 : -1) * (baseSpeed * spec.speedBonus),
                vy: (mode === 'breaking') ? 0 : (Math.random() - 0.5) * (baseSpeed * spec.speedBonus)
            };
        }

        function startSession() {
            if (isPlaying) return;
            isPlaying = true;
            canvas.style.cursor = "none";
            score = 0; timeLeft = 30.0; totalShots = 0; hitShots = 0;
            playerLives = 2; // 브레이킹용 목숨 리셋
            playerX = 430; playerVx = 0; enemyShootTimer = 0; projectiles = [];
            initTargets();
            document.getElementById('start-btn').style.background = '#4b5563';
            document.getElementById('start-btn').innerText = "⏱ 훈련 진행중";
            document.getElementById('quit-btn').style.display = "inline-block";
        }

        // 🚪 일시정지 대신 완벽한 이탈/종료 기능 구현
        function quitSession() {
            isPlaying = false;
            canvas.style.cursor = "default";
            document.getElementById('start-btn').style.background = '#34d399';
            document.getElementById('start-btn').innerText = "▶ 훈련 시작";
            document.getElementById('quit-btn').style.display = "none";
            projectiles = [];
            updateDashboard();
        }

        function endSession() {
            isPlaying = false;
            canvas.style.cursor = "default";
            document.getElementById('start-btn').style.background = '#34d399';
            document.getElementById('start-btn').innerText = "▶ 훈련 시작";
            document.getElementById('quit-btn').style.display = "none";

            if (score > (highScores[mode] || 0)) { 
                highScores[mode] = score; 
                saveScores(); 
                renderScoresUI(); 
            }
        }

        // 단발성 클릭 히트 판정 (그리드샷, 마이크로플렉스, 브레이킹 전용)
        canvas.addEventListener('mousedown', () => {
            if (!isPlaying) return;
            if (mode === 'tracking') return;

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
                    playKillSound(); // 킬사운드 방출
                    targets[i] = generateTargetData(); break;
                }
            }
            if (!hitAny) score = Math.max(0, score - 20);
            updateDashboard();
        });

        function updateDashboard() {
            document.getElementById('ui-score').innerText = "SCORE: " + score;
            let acc = totalShots > 0 ? Math.round((hitShots / totalShots) * 100) : 100;
            if (mode === 'tracking') acc = 100;
            document.getElementById('ui-acc').innerText = "ACC: " + acc + "%";
            document.getElementById('ui-time').innerText = "TIME: " + timeLeft.toFixed(1) + "s";
        }

        function loop() {
            if (showHitEffect && hitEffectTimer > 0) {
                ctx.fillStyle = '#260a0f'; hitEffectTimer--;
                if(hitEffectTimer <= 0) showHitEffect = false;
            } else {
                ctx.fillStyle = '#090b11';
            }
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 격자 배경선 드로잉
            ctx.strokeStyle = '#121620'; ctx.lineWidth = 1;
            for(let i=0; i<canvas.width; i+=50) { ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,canvas.height); ctx.stroke(); }
            for(let j=0; j<canvas.height; j+=50) { ctx.beginPath(); ctx.moveTo(0,j); ctx.lineTo(canvas.width,j); ctx.stroke(); }

            // 플레이어 좌우 이동 관성 계산
            if (keys.a) playerVx = Math.max(-playerMaxSpeed, playerVx - playerAcc);
            else if (keys.d) playerVx = Math.min(playerMaxSpeed, playerVx + playerAcc);
            else {
                if (playerVx > 0) playerVx = Math.max(0, playerVx - playerFric);
                else if (playerVx < 0) playerVx = Math.min(0, playerVx + playerFric);
            }
            playerX = Math.max(40, Math.min(canvas.width - 40, playerX + playerVx));

            // 브레이킹 모드 전용 무빙샷 탄퍼짐 구현
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

                // 🔄 [트래킹 모드 코어 메커니즘 정상화 및 전용 점수 연산]
                if (mode === 'tracking' && isMouseDown) {
                    targets.forEach((t) => {
                        let dist = Math.hypot(mouseX - t.x, mouseY - t.y);
                        if (dist <= t.radius) {
                            score += 2; // 누르고 과녁 조준 유지 시 점수 실시간 업
                        }
                    });
                }

                // VAL-BREAKING 전용: 투사체 발사 타이머 연산
                if (mode === 'breaking') {
                    enemyShootTimer++;
                    let shootInterval = difficulty === 1 ? 70 : (difficulty === 2 ? 50 : (difficulty === 3 ? 35 : 24));
                    if (enemyShootTimer >= shootInterval && targets.length > 0) {
                        enemyShootTimer = 0;
                        let t = targets[0];
                        let dx = playerX - t.x;
                        let dy = (canvas.height - 20) - t.y;
                        let dist = Math.hypot(dx, dy);
                        let speed = diffSpecs[difficulty].projectileSpeed;
                        projectiles.push({
                            x: t.x, y: t.y,
                            vx: (dx / dist) * speed,
                            vy: (dy / dist) * speed,
                            radius: 6
                        });
                    }
                }

                // 투사체 이동 및 캐릭터 2회 피격 사망 연산
                for (let i = projectiles.length - 1; i >= 0; i--) {
                    let p = projectiles[i];
                    p.x += p.vx; p.y += p.vy;

                    if (p.y >= canvas.height - 25 && p.y <= canvas.height - 10) {
                        if (p.x >= playerX - 30 && p.x <= playerX + 30) {
                            // 대미지 발생
                            playerLives--;
                            showHitEffect = true; hitEffectTimer = 10;
                            projectiles.splice(i, 1);
                            
                            // 💔 2회 피격 시 즉시 종료 (게임오버) 사양 작동
                            if (playerLives <= 0) {
                                quitSession();
                                alert("💥 미사일에 2회 피격되었습니다! 게임 오버!");
                                break;
                            }
                            continue;
                        }
                    }

                    if (p.y > canvas.height || p.x < 0 || p.x > canvas.width) { projectiles.splice(i, 1); continue; }

                    ctx.save(); ctx.fillStyle = '#f59e0b'; ctx.shadowColor = '#ef4444'; ctx.shadowBlur = 8;
                    ctx.beginPath(); ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2); ctx.fill(); ctx.restore();
                }

                // 모든 타겟들의 물리 바운딩 처리 및 렌더링
                targets.forEach((t) => {
                    t.x += t.vx; t.y += t.vy;
                    if(t.x - t.radius < 15 || t.x + t.radius > canvas.width - 15) t.vx *= -1;
                    if(t.y - t.radius < 15 || t.y + t.radius > canvas.height - 15) t.vy *= -1;

                    ctx.save();
                    if(mode === 'gridshot') ctx.strokeStyle = '#38bdf8';
                    else if(mode === 'tracking') { ctx.strokeStyle = '#00f2fe'; ctx.fillStyle = 'rgba(0, 242, 254, 0.1)'; ctx.fill(); } // 트래킹 타겟 가시성 확보
                    else if(mode === 'microflex') ctx.strokeStyle = '#f43f5e';
                    else { ctx.strokeStyle = '#ff4655'; ctx.shadowColor = '#ff4655'; ctx.shadowBlur = 6; }
                    
                    ctx.lineWidth = 2.5;
                    ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI*2); ctx.stroke();
                    ctx.restore();
                });
            } else {
                ctx.fillStyle = 'rgba(255,255,255,0.25)'; ctx.font = '14px sans-serif'; ctx.textAlign = 'center';
                ctx.fillText("원하는 설정을 마치고 상단 [▶ 훈련 시작]을 클릭하세요.", canvas.width/2, canvas.height/2 - 20);
                ctx.fillText("VAL-BREAKING 모드: 2번 피격되면 즉시 탈락합니다! 조심하세요!", canvas.width/2, canvas.height/2 + 10);
            }

            if (showMovingError && errorTimer > 0) {
                ctx.save(); ctx.fillStyle = '#ff4655'; ctx.font = 'bold 20px sans-serif'; ctx.textAlign = 'center';
                ctx.fillText("❌ 무빙샷 불허 (탄퍼짐 발생!)", canvas.width/2, 70); ctx.restore();
                errorTimer--; if(errorTimer <= 0) showMovingError = false;
            }

            // 하단 플레이어 바 및 목숨(Life) 텍스트 렌더링
            ctx.save();
            ctx.fillStyle = Math.abs(playerVx) <= 0.2 ? '#22c55e' : '#eab308';
            ctx.fillRect(playerX - 25, canvas.height - 25, 50, 10);
            
            ctx.fillStyle = '#e5e7eb'; ctx.font = '11px sans-serif'; ctx.textAlign = 'center';
            if (mode === 'breaking' && isPlaying) {
                let heartStr = playerLives === 2 ? "❤️ ❤️" : "❤️ 💔";
                ctx.fillText("HP: " + heartStr, playerX, canvas.height - 35);
            } else {
                ctx.fillText("PLAYER", playerX, canvas.height - 35);
            }
            ctx.restore();

            // 빨간 점 조준선 고정 드로잉
            ctx.save(); ctx.fillStyle = '#FF0000';
            ctx.beginPath(); ctx.arc(mouseX, mouseY, 3.5, 0, Math.PI * 2); ctx.fill(); ctx.restore();

            requestAnimationFrame(loop);
        }

        loadSavedScores(); initTargets(); loop();
    </script>
    """
    st.components.v1.html(html_src, height=590)

if __name__ == "__main__":
    main()
