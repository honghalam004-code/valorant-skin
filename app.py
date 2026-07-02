import streamlit as st

def main():
    st.set_page_config(page_title="AIMLAB + VALORANT ALL-IN-ONE", layout="wide")

    st.markdown("""
        <style>
        .main { background-color: #070913; color: #e5e7eb; font-family: 'Segoe UI', monospace; }
        iframe { border: none !important; }
        .section-title {
            color: #ff4655; font-weight: 900; letter-spacing: 2px; 
            border-bottom: 2px solid #1f293d; padding-bottom: 8px; margin-top: 30px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center; color:#ff4655; font-weight:900;'>🎯 AIM TRAINING ULTIMATE TRILOGY</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#6b7280; font-size:14px;'>메인 에임랩 + 자동 미니게임 + 발로란트 연습장 통합 패키지 (웅장한 타격 킬사운드 탑재)</p>", unsafe_allow_html=True)

    html_src = """
    <div style="max-width:1200px; margin:0 auto; display:flex; flex-direction:column; gap:35px;">
        
        <h3 class="section-title" style="color:#00f2fe; border-color:#00f2fe;">STAGE 01 : MAIN AIMLAB REBOOT</h3>
        <div style="display:flex; gap:20px; justify-content:center;">
            <div style="flex: 1; text-align:center;">
                <div style="display:flex; justify-content:space-between; align-items:center; background:#111625; padding:12px 20px; border-radius:6px; margin-bottom:12px; border:1px solid #1f2942;">
                    <div style="display:flex; gap:6px;">
                        <button onclick="changeMode('gridshot')" id="m-grid" style="background:#00f2fe; color:black; border:none; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">🎯 GRIDSHOT</button>
                        <button onclick="changeMode('tracking')" id="m-track" style="background:#07080b; color:#00f2fe; border:1px solid #00f2fe; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">🔄 TRACKING</button>
                        <button onclick="changeMode('microflex')" id="m-micro" style="background:#07080b; color:#00f2fe; border:1px solid #00f2fe; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">⚡ MICROFLEX</button>
                        <button onclick="changeMode('breaking')" id="m-break" style="background:#07080b; color:#ff4655; border:1px solid #ff4655; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">⚡ VAL-BREAKING</button>
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
                <canvas id="aimCanvas" width="880" height="420" style="background:#090b15; border:2px solid #1f2942; border-radius:6px; cursor:none;"></canvas>
            </div>

            <div style="width:260px; display:flex; flex-direction:column; gap:12px;">
                <div style="background:#111625; padding:14px; border-radius:6px; border:1px solid #1f2942;">
                    <div style="color:#ff4655; font-size:11px; font-weight:bold; margin-bottom:6px;">⚙️ SENSITIVITY</div>
                    <input type="range" id="sens-slider" min="0.1" max="4.0" step="0.05" value="1.0" oninput="updateSensitivity(this.value)" style="width:100%; accent-color:#ff4655;">
                    <div style="text-align:right; font-size:14px; font-weight:bold; color:#ff4655; margin-top:4px;" id="sens-val">1.00</div>
                </div>
                <div style="background:#111625; padding:14px; border-radius:6px; border:1px solid #1f2942; flex:1;">
                    <div style="color:#00f2fe; font-size:11px; font-weight:bold; margin-bottom:8px;">🏆 REBOOT RECORDS</div>
                    <div id="record-board" style="font-family:monospace; font-size:12px; display:flex; flex-direction:column; gap:8px;"></div>
                </div>
            </div>
        </div>

        <h3 class="section-title" style="color:#a855f7; border-color:#a855f7;">STAGE 02 : AUTOMATIC AIM POP (MINI GAME)</h3>
        <div style="background:#111625; padding:20px; border-radius:8px; border:1px solid #1f2942; display:flex; gap:25px; align-items:center;">
            <div style="flex:1;">
                <p style="margin:0 0 10px 0; color:#e5e7eb; font-size:14px; font-weight:bold;">💡 별도의 시작 버튼이 없는 무한 에임 서프 판입니다!</p>
                <p style="margin:0 0 15px 0; color:#9ca3af; font-size:12px; line-height:1.5;">오른쪽 캔버스 내부로 마우스 커서를 가져가면 풍선 표적들이 자동으로 스폰되기 시작합니다. 커서가 밖으로 이탈하면 자동으로 대기 상태로 전환됩니다.</p>
                <div style="display:flex; gap:15px; font-family:monospace; font-size:14px; font-weight:bold; background:#070913; padding:12px; border-radius:6px; border:1px solid #1f2942;">
                    <div style="color:#a855f7;" id="mini-score">SCORE: 0</div>
                    <div style="color:#34d399;" id="mini-combo">COMBO: 0</div>
                </div>
            </div>
            <canvas id="miniCanvas" width="620" height="200" style="background:#070913; border:2px dashed #a855f7; border-radius:6px; cursor:crosshair;"></canvas>
        </div>

        <h3 class="section-title" style="color:#ff4655; border-color:#ff4655;">STAGE 03 : VALORANT THE RANGE (사격 연습장)</h3>
        <div style="background:#111625; padding:15px; border-radius:8px; border:1px solid #1f2942; text-align:center;">
            <p style="margin:0 0 10px 0; color:#9ca3af; font-size:12px;">※ 내부의 전광판 오브젝트 <b>[ 🤖 START CHALLENGE ]</b> 와 <b>[ 🤖 RESPAWN ]</b> 판을 직접 사격하여 가동/이탈 제어하세요.</p>
            <canvas id="rangeCanvas" width="1160" height="380" style="background:#0b0e14; border:2px solid #ff4655; border-radius:6px; cursor:none;"></canvas>
        </div>

    </div>

    <script>
        // --- 엔진 3사 캔버스 정렬 바인딩 ---
        const canvas = document.getElementById('aimCanvas'); const ctx = canvas.getContext('2d');
        const miniCanvas = document.getElementById('miniCanvas'); const miniCtx = miniCanvas.getContext('2d');
        const rangeCanvas = document.getElementById('rangeCanvas'); const rangeCtx = rangeCanvas.getContext('2d');

        // --- 🎵 오디오 리뉴얼: 심장이 울리는 웅장한 시네마틱 킬 사운드 엔진 ---
        let audioCtx = null;
        function playGrandKillSound() {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                
                let now = audioCtx.currentTime;

                // 1. 웅장하게 바닥을 깔아주는 저주파 서브 우퍼 폭발 효과음
                let subOsc = audioCtx.createOscillator();
                let subGain = audioCtx.createGain();
                subOsc.type = 'sine';
                subOsc.frequency.setValueAtTime(140, now);
                subOsc.frequency.exponentialRampToValueAtTime(45, now + 0.35); // 묵직하게 하강하는 저음 베이스
                subGain.gain.setValueAtTime(0.4, now);
                subGain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
                subOsc.connect(subGain); subGain.connect(audioCtx.destination);
                subOsc.start(now); subOsc.stop(now + 0.35);

                // 2. 가슴 속을 긁어주는 댐핑 디스토션 크런치 효과음
                let midOsc = audioCtx.createOscillator();
                let midGain = audioCtx.createGain();
                midOsc.type = 'triangle';
                midOsc.frequency.setValueAtTime(280, now);
                midOsc.frequency.linearRampToValueAtTime(90, now + 0.18);
                midGain.gain.setValueAtTime(0.25, now);
                midGain.gain.exponentialRampToValueAtTime(0.001, now + 0.18);
                midOsc.connect(midGain); midGain.connect(audioCtx.destination);
                midOsc.start(now); midOsc.stop(now + 0.18);

                // 3. 고주파 잔향 스냅 (헤드샷 금속성 타격 레이어)
                let snapOsc = audioCtx.createOscillator();
                let snapGain = audioCtx.createGain();
                snapOsc.type = 'sine';
                snapOsc.frequency.setValueAtTime(1250, now);
                snapGain.gain.setValueAtTime(0.1, now);
                snapGain.gain.exponentialRampToValueAtTime(0.001, now + 0.06);
                snapOsc.connect(snapGain); snapGain.connect(audioCtx.destination);
                snapOsc.start(now); snapOsc.stop(now + 0.06);
            } catch(e) {}
        }

        // ========================================================
        // [DATA & CORE 1] STAGE 1 에임랩 전용 컴포넌트
        // ========================================================
        let mode = 'gridshot'; let isPlaying = false; let score = 0; let timeLeft = 30.0;
        let totalShots = 0; let hitShots = 0; let playerLives = 2;
        let mouseX = 440, mouseY = 210; let rawMouseX = 440, rawMouseY = 210; let isMouseDown = false;
        let playerX = 440; let playerVx = 0; let keys = { a: false, d: false };
        let showMovingError = false; let errorTimer = 0;
        let projectiles = []; let enemyShootTimer = 0; let showHitEffect = false; let hitEffectTimer = 0;
        let highScores = { gridshot: 0, tracking: 0, microflex: 0, breaking: 0 };
        let targets = [];

        // ========================================================
        // [DATA & CORE 2] STAGE 2 미니게임 전용 컴포넌트 (자동 가동형)
        // ========================================================
        let isMiniHovered = false; let miniScore = 0; let miniCombo = 0; let miniTargets = [];

        // ========================================================
        // [DATA & CORE 3] STAGE 3 발로란트 연습장 전용 컴포넌트
        // ========================================================
        let isRangePlaying = false; let rangeScore = 0; let rangeTimeLeft = 30.0;
        let rangeX = 580; let rangeVx = 0; let rangeBotShootTimer = 0; let rangeProjectiles = [];
        let rangeBots = []; let rMouseX = 580, rMouseY = 190;
        const rangeUIBox = [
            { id: 'start', x: 440, y: 40, w: 140, h: 30, label: "🤖 START CHALLENGE" },
            { id: 'respawn', x: 600, y: 40, w: 100, h: 30, label: "🤖 RESPAWN" }
        ];

        // --- 마우스 및 키보드 바인딩 리스너 ---
        window.addEventListener('keydown', (e) => {
            if (e.key.toLowerCase() === 'a') keys.a = true;
            if (e.key.toLowerCase() === 'd') keys.d = true;
        });
        window.addEventListener('keyup', (e) => {
            if (e.key.toLowerCase() === 'a') keys.a = false;
            if (e.key.toLowerCase() === 'd') keys.d = false;
        });

        // 1단 마우스 제어
        canvas.addEventListener('mousemove', (e) => {
            let rect = canvas.getBoundingClientRect(); rawMouseX = e.clientX - rect.left; rawMouseY = e.clientY - rect.top;
        });
        canvas.addEventListener('mousedown', () => { isMouseDown = true; handleMainClick(); });
        window.addEventListener('mouseup', () => { isMouseDown = false; });

        // 2단 마우스 제어 (자동 인터랙션 감지 기믹)
        miniCanvas.addEventListener('mouseenter', () => { isMiniHovered = true; });
        miniCanvas.addEventListener('mouseleave', () => { isMiniHovered = false; miniCombo = 0; document.getElementById('mini-combo').innerText = "COMBO: 0"; });
        miniCanvas.addEventListener('mousedown', (e) => {
            let rect = miniCanvas.getBoundingClientRect();
            let mX = e.clientX - rect.left; let mY = e.clientY - rect.top;
            let hit = false;
            for(let i = miniTargets.length - 1; i >= 0; i--) {
                let t = miniTargets[i];
                if (Math.hypot(mX - t.x, mY - t.y) <= t.r) {
                    miniScore += 100 + (miniCombo * 10); miniCombo++; hit = true;
                    playGrandKillSound(); // 웅장한 사운드 적용
                    miniTargets.splice(i, 1); break;
                }
            }
            if(!hit) { miniCombo = 0; miniScore = Math.max(0, miniScore - 30); }
            document.getElementById('mini-score').innerText = "SCORE: " + miniScore;
            document.getElementById('mini-combo').innerText = "COMBO: " + miniCombo;
        });

        // 3단 마우스 제어 (발로란트 연습장)
        rangeCanvas.addEventListener('mousemove', (e) => {
            let rect = rangeCanvas.getBoundingClientRect(); rMouseX = e.clientX - rect.left; rMouseY = e.clientY - rect.top;
        });
        rangeCanvas.addEventListener('mousedown', () => { handleRangeClick(); });


        // --- 에임랩 1단 제어 서브 함수 ---
        function handleMainClick() {
            if (!isPlaying || mode === 'tracking') return;
            totalShots++; let hitAny = false;
            for (let i = 0; i < targets.length; i++) {
                if (Math.hypot(mouseX - targets[i].x, mouseY - targets[i].y) <= targets[i].radius) {
                    if (mode === 'breaking' && Math.abs(playerVx) > 0.2) {
                        score = Math.max(0, score - 40); showMovingError = true; errorTimer = 25; return;
                    }
                    hitShots++; score += 100; hitAny = true;
                    playGrandKillSound(); targets[i] = generateTargetData(); break;
                }
            }
            if (!hitAny) score = Math.max(0, score - 20);
            updateDashboard();
        }

        function updateSensitivity(val) {
            sensitivity = parseFloat(val); document.getElementById('sens-val').innerText = sensitivity.toFixed(2);
        }

        function changeMode(m) {
            mode = m;
            ['grid', 'track', 'micro', 'break'].forEach(k => {
                const el = document.getElementById('m-' + k);
                let targetKey = m.substring(0,5); if (m === 'breaking') targetKey = 'break';
                if (k === targetKey) { el.style.background = m === 'breaking' ? '#ff4655' : '#00f2fe'; el.style.color = 'black'; el.style.border = 'none'; } 
                else { el.style.background = '#07080b'; el.style.color = k === 'break' ? '#ff4655' : '#00f2fe'; el.style.border = '1px solid currentColor'; }
            });
            quitSession(); initTargets(); updateDashboard();
        }

        function initTargets() {
            targets = []; projectiles = []; let count = (mode === 'gridshot') ? 3 : 1;
            for(let i=0; i<count; i++) targets.push(generateTargetData());
        }

        function generateTargetData() {
            let baseRadius = 16; let baseSpeed = 3.0;
            if (mode === 'tracking') { baseRadius = 20; baseSpeed = 4.2; }
            else if (mode === 'microflex') { baseRadius = 11; baseSpeed = 3.5; }
            else if (mode === 'breaking') { baseRadius = 16; baseSpeed = 2.0; }
            return {
                x: 100 + Math.random() * (canvas.width - 200),
                y: 80 + Math.random() * (mode === 'breaking' ? 70 : (canvas.height - 180)),
                radius: baseRadius,
                vx: (Math.random() > 0.5 ? 1 : -1) * baseSpeed,
                vy: (mode === 'breaking') ? 0 : (Math.random() - 0.5) * baseSpeed
            };
        }

        function startSession() {
            isPlaying = true; score = 0; timeLeft = 30.0; totalShots = 0; hitShots = 0; playerLives = 2; projectiles = [];
            initTargets();
            document.getElementById('start-btn').style.background = '#4b5563'; document.getElementById('start-btn').innerText = "⏱ 진행중";
            document.getElementById('quit-btn').style.display = "inline-block";
        }

        function quitSession() {
            isPlaying = false; document.getElementById('start-btn').style.background = '#34d399'; document.getElementById('start-btn').innerText = "▶ 훈련 시작";
            document.getElementById('quit-btn').style.display = "none"; projectiles = []; updateDashboard();
        }

        function updateDashboard() {
            document.getElementById('ui-score').innerText = "SCORE: " + score;
            let acc = totalShots > 0 ? Math.round((hitShots / totalShots) * 100) : 100;
            document.getElementById('ui-acc').innerText = "ACC: " + (mode==='tracking'?100:acc) + "%";
            document.getElementById('ui-time').innerText = "TIME: " + timeLeft.toFixed(1) + "s";
        }

        function renderScoresUI() {
            document.getElementById('record-board').innerHTML = `
                <div style="display:flex; justify-content:space-between; margin-top:2px;"><span>🎯 GRIDSHOT</span><span style="color:#38bdf8; font-weight:bold;">${highScores.gridshot}</span></div>
                <div style="display:flex; justify-content:space-between;"><span>🔄 TRACKING</span><span style="color:#00f2fe; font-weight:bold;">${highScores.tracking}</span></div>
                <div style="display:flex; justify-content:space-between;"><span>⚡ MICROFLEX</span><span style="color:#f43f5e; font-weight:bold;">${highScores.microflex}</span></div>
                <div style="display:flex; justify-content:space-between; border-top:1px dashed #ff4655; padding-top:4px; margin-top:4px;"><span>💥 BREAKING</span><span style="color:#ff4655; font-weight:bold;">${highScores.breaking}</span></div>
            `;
        }

        // --- 발로란트 연습장 3단 제어 서브 함수 ---
        function handleRangeClick() {
            // 상단 액션판 확인
            for(let i=0; i<rangeUIBox.length; i++) {
                let box = rangeUIBox[i];
                if (rMouseX >= box.x && rMouseX <= box.x + box.w && rMouseY >= box.y && rMouseY <= box.y + box.h) {
                    playGrandKillSound();
                    if (box.id === 'start' && !isRangePlaying) { isRangePlaying = true; rangeScore = 0; rangeTimeLeft = 30.0; initRangeBots(); }
                    if (box.id === 'respawn') { isRangePlaying = false; rangeBots = []; rangeProjectiles = []; }
                    return;
                }
            }
            if (!isRangePlaying) return;
            let hit = false;
            for(let i = rangeBots.length - 1; i >= 0; i--) {
                if (Math.hypot(rMouseX - rangeBots[i].x, rMouseY - rangeBots[i].y) <= rangeBots[i].r) {
                    rangeScore += 100; hit = true;
                    playGrandKillSound(); rangeBots.splice(i, 1);
                    rangeBots.push(generateRangeBotData()); break;
                }
            }
            if(!hit) rangeScore = Math.max(0, rangeScore - 20);
        }

        function initRangeBots() { rangeBots = [generateRangeBotData(), generateRangeBotData()]; }
        function generateRangeBotData() {
            return {
                x: 100 + Math.random() * (rangeCanvas.width - 200), y: 150 + Math.random() * 140, r: 15,
                vx: (Math.random() > 0.5 ? 1 : -1) * 2.5
            };
        }


        // ========================================================
        // 🔄 통합 루프 스케줄러 (3개 게임을 하나의 FPS 프레임으로 동시 연산)
        // ========================================================
        function loop() {
            // --- STAGE 1 연산 ---
            if (showHitEffect && hitEffectTimer > 0) { ctx.fillStyle = '#220d11'; hitEffectTimer--; if(hitEffectTimer<=0) showHitEffect=false; } 
            else { ctx.fillStyle = '#090b15'; }
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            if (keys.a) playerVx = Math.max(-5.5, playerVx - 0.8);
            else if (keys.d) playerVx = Math.min(5.5, playerVx + 0.8);
            else { playerVx *= 0.6; }
            playerX = Math.max(40, Math.min(canvas.width - 40, playerX + playerVx));
            mouseX = rawMouseX; mouseY = rawMouseY;

            if (isPlaying) {
                timeLeft -= 1/60; if (timeLeft <= 0) { timeLeft = 0; isPlaying = false; if(score>highScores[mode]){highScores[mode]=score; renderScoresUI();} quitSession(); }
                if (mode === 'tracking' && isMouseDown) {
                    targets.forEach(t => { if(Math.hypot(mouseX-t.x, mouseY-t.y)<=t.radius) score+=2; });
                }
                if (mode === 'breaking') {
                    enemyShootTimer++;
                    if(enemyShootTimer >= 55) {
                        enemyShootTimer = 0; let t = targets[0];
                        let dx = playerX - t.x; let dy = (canvas.height - 20) - t.y; let dist = Math.hypot(dx, dy);
                        projectiles.push({ x: t.x, y: t.y, vx: (dx/dist)*4, vy: (dy/dist)*4, radius: 5 });
                    }
                }
                for (let i = projectiles.length - 1; i >= 0; i--) {
                    let p = projectiles[i]; p.x += p.vx; p.y += p.vy;
                    if (p.y >= canvas.height - 25 && p.y <= canvas.height - 10 && p.x >= playerX - 25 && p.x <= playerX + 25) {
                        playerLives--; showHitEffect = true; hitEffectTimer = 10; projectiles.splice(i, 1);
                        if (playerLives <= 0) { quitSession(); alert("💥 브레이킹 모드 사망 (2회 피격)"); } continue;
                    }
                    if (p.y > canvas.height) { projectiles.splice(i, 1); continue; }
                    ctx.fillStyle = '#f59e0b'; ctx.beginPath(); ctx.arc(p.x, p.y, p.radius, 0, Math.PI*2); ctx.fill();
                }
                targets.forEach(t => {
                    t.x += t.vx; t.y += t.vy;
                    if(t.x - t.radius < 10 || t.x + t.radius > canvas.width - 10) t.vx *= -1;
                    if(t.y - t.radius < 10 || t.y + t.radius > canvas.height - 10) t.vy *= -1;
                    ctx.strokeStyle = mode==='breaking'?'#ff4655':'#00f2fe'; ctx.lineWidth = 2.5;
                    ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI*2); ctx.stroke();
                });
            }
            ctx.fillStyle = Math.abs(playerVx) <= 0.2 ? '#22c55e' : '#eab308'; ctx.fillRect(playerX - 20, canvas.height - 20, 40, 8);
            ctx.fillStyle = '#ff4655'; ctx.beginPath(); ctx.arc(mouseX, mouseY, 3.5, 0, Math.PI*2); ctx.fill();


            // --- STAGE 2 연산 (미니게임) ---
            miniCtx.fillStyle = '#070913'; miniCtx.fillRect(0, 0, miniCanvas.width, miniCanvas.height);
            if (isMiniHovered) {
                if (miniTargets.length < 4 && Math.random() < 0.05) {
                    miniTargets.push({ x: 30 + Math.random()*(miniCanvas.width-60), y: 30 + Math.random()*(miniCanvas.height-60), r: 0, maxR: 14+Math.random()*10, grow: true });
                }
                for(let i=miniTargets.length-1; i>=0; i--) {
                    let mt = miniTargets[i];
                    if(mt.grow) { mt.r += 0.4; if(mt.r >= mt.maxR) mt.grow = false; } 
                    else { mt.r -= 0.25; if(mt.r <= 2) { miniTargets.splice(i, 1); miniCombo = 0; document.getElementById('mini-combo').innerText = "COMBO: 0"; continue; } }
                    miniCtx.fillStyle = 'rgba(168, 85, 247, 0.25)'; miniCtx.beginPath(); miniCtx.arc(mt.x, mt.y, mt.r, 0, Math.PI*2); miniCtx.fill();
                    miniCtx.strokeStyle = '#a855f7'; miniCtx.lineWidth = 1.5; miniCtx.stroke();
                }
            } else {
                miniCtx.fillStyle = '#4b5563'; miniCtx.font = '12px sans-serif'; miniCtx.textAlign = 'center';
                miniCtx.fillText("이곳에 마우스를 올리면 과녁이 자동으로 깨어납니다.", miniCanvas.width/2, miniCanvas.height/2);
            }


            // --- STAGE 3 연산 (발로란트 연습장) ---
            rangeCtx.fillStyle = '#0b0e14'; rangeCtx.fillRect(0, 0, rangeCanvas.width, rangeCanvas.height);
            // 가이드 UI 판넬
            rangeUIBox.forEach(box => {
                rangeCtx.fillStyle = box.id === 'start' ? (isRangePlaying ? '#374151' : '#047857') : '#b91c1c';
                rangeCtx.fillRect(box.x, box.y, box.w, box.h);
                rangeCtx.fillStyle = '#ffffff'; rangeCtx.font = 'bold 11px sans-serif'; rangeCtx.textAlign = 'center';
                rangeCtx.fillText(box.label, box.x + box.w/2, box.y + box.h/1.6);
            });

            // 실시간 스코어보드 렌더링
            rangeCtx.fillStyle = '#e5e7eb'; rangeCtx.font = 'bold 14px monospace'; rangeCtx.textAlign = 'left';
            rangeCtx.fillText(`[THE RANGE STATS] SCORE: ${rangeScore} | TIME: ${rangeTimeLeft.toFixed(1)}s`, 40, 60);

            // 발로란트 연습장 이동 발판 가동
            if (keys.a) rangeVx = Math.max(-5.0, rangeVx - 0.7);
            else if (keys.d) rangeVx = Math.min(5.0, rangeVx + 0.7);
            else { rangeVx *= 0.6; }
            rangeX = Math.max(50, Math.min(rangeCanvas.width - 50, rangeX + rangeVx));

            if (isRangePlaying) {
                rangeTimeLeft -= 1/60; if(rangeTimeLeft <= 0) { rangeTimeLeft = 0; isRangePlaying = false; }
                
                // 연습장 봇 무빙 및 렌더링
                rangeBots.forEach(b => {
                    b.x += b.vx; if(b.x - b.r < 20 || b.x + b.r > rangeCanvas.width - 20) b.vx *= -1;
                    let bGrad = rangeCtx.createRadialGradient(b.x, b.y, 2, b.x, b.y, b.r);
                    bGrad.addColorStop(0, '#ffffff'); bGrad.addColorStop(1, '#ff4655');
                    rangeCtx.fillStyle = bGrad; rangeCtx.beginPath(); rangeCtx.arc(b.x, b.y, b.r, 0, Math.PI*2); rangeCtx.fill();
                    rangeCtx.strokeStyle = '#ffffff'; rangeCtx.stroke();
                });

                // 연습장 무빙샷 탄퍼짐 라인 계산 및 실시간 십자선 페인팅
                rangeCtx.save(); rangeCtx.strokeStyle = '#ff4655'; rangeCtx.lineWidth = 1.5;
                let s = Math.abs(rangeVx) * 1.5;
                rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX - 6 - s, rMouseY); rangeCtx.lineTo(rMouseX + 6 + s, rMouseY); rangeCtx.stroke();
                rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX, rMouseY - 6 - s); rangeCtx.lineTo(rMouseX, rMouseY + 6 + s); rangeCtx.stroke();
                rangeCtx.restore();
            } else {
                rangeCtx.fillStyle = '#4b5563'; rangeCtx.font = '13px sans-serif'; rangeCtx.textAlign = 'center';
                rangeCtx.fillText("상단의 [🤖 START CHALLENGE] 과녁판을 조준 사격하면 디펜스 훈련이 가동됩니다.", rangeCanvas.width/2, rangeCanvas.height/2 + 20);
                // 기본 대기 크로스헤어
                rangeCtx.strokeStyle = '#ff4655'; rangeCtx.lineWidth = 1.5;
                rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX-6, rMouseY); rangeCtx.lineTo(rMouseX+6, rMouseY); rangeCtx.stroke();
                rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX, rMouseY-6); rangeCtx.lineTo(rMouseX, rMouseY+6); rangeCtx.stroke();
            }
            rangeCtx.fillStyle = '#38bdf8'; rangeCtx.fillRect(rangeX - 25, rangeCanvas.height - 20, 50, 6);

            requestAnimationFrame(loop);
        }

        highScores = { gridshot: 0, tracking: 0, microflex: 0, breaking: 0 }; renderScoresUI(); initTargets(); loop();
    </script>
    """
    st.components.v1.html(html_src, height=1280)

if __name__ == "__main__":
    main()
