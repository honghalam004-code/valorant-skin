import streamlit as st

def main():
    st.set_page_config(page_title="AIMLAB ULTIMATE TRILOGY", layout="wide")

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

    html_src = """
    <div style="max-width:1200px; margin:0 auto; display:flex; flex-direction:column; gap:35px;">
        
        <h3 class="section-title" style="color:#00f2fe; border-color:#00f2fe;">STAGE 01 : MAIN AIMLAB (난이도 선택 탑재)</h3>
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
                        <button onclick="quitSession()" id="quit-btn" style="background:#ef4444; color:white; border:none; padding:8px 14px; font-weight:bold; cursor:pointer; border-radius:4px; display:none;">🚪 나가기</button>
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
                
                <div style="background:#111625; padding:14px; border-radius:6px; border:1px solid #1f2942;">
                    <div style="color:#00f2fe; font-size:11px; font-weight:bold; margin-bottom:8px;">📊 난이도 레벨 설정</div>
                    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:6px;">
                        <button onclick="setDifficulty(1)" id="df-1" style="background:#22c55e; color:black; border:none; padding:8px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">레벨 1</button>
                        <button onclick="setDifficulty(2)" id="df-2" style="background:#07080b; color:#e5e7eb; border:1px solid #374151; padding:8px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">레벨 2</button>
                        <button onclick="setDifficulty(3)" id="df-3" style="background:#07080b; color:#e5e7eb; border:1px solid #374151; padding:8px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">레벨 3</button>
                        <button onclick="setDifficulty(4)" id="df-4" style="background:#07080b; color:#e5e7eb; border:1px solid #374151; padding:8px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">레벨 4</button>
                    </div>
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
                <p style="margin:0 0 10px 0; color:#e5e7eb; font-size:14px; font-weight:bold;">💡 마우스만 올리면 켜지는 무한 팝핑 서프 판</p>
                <div style="display:flex; gap:15px; font-family:monospace; font-size:14px; font-weight:bold; background:#070913; padding:12px; border-radius:6px; border:1px solid #1f2942;">
                    <div style="color:#a855f7;" id="mini-score">SCORE: 0</div>
                    <div style="color:#34d399;" id="mini-combo">COMBO: 0</div>
                </div>
            </div>
            <canvas id="miniCanvas" width="620" height="200" style="background:#070913; border:2px dashed #a855f7; border-radius:6px; cursor:crosshair выполнен;"></canvas>
        </div>

        <h3 class="section-title" style="color:#ff4655; border-color:#ff4655;">STAGE 03 : VALORANT THE RANGE (사격 연습장)</h3>
        <div style="background:#111625; padding:15px; border-radius:8px; border:1px solid #1f2942; text-align:center;">
            <canvas id="rangeCanvas" width="1160" height="380" style="background:#0b0e14; border:2px solid #ff4655; border-radius:6px; cursor:none;"></canvas>
        </div>

    </div>

    <script>
        const canvas = document.getElementById('aimCanvas'); const ctx = canvas.getContext('2d');
        const miniCanvas = document.getElementById('miniCanvas'); const miniCtx = miniCanvas.getContext('2d');
        const rangeCanvas = document.getElementById('rangeCanvas'); const rangeCtx = rangeCanvas.getContext('2d');

        // --- 🎵 오디오 리뉴얼: 발로란트식 웅장하고 깊은 메탈릭 타격 킬사운드 ---
        let audioCtx = null;
        function playGrandKillSound() {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                
                let now = audioCtx.currentTime;

                // 1. 심장을 때리는 가슴이 웅장해지는 저음 우퍼 폭발음 (Bass Damping)
                let subOsc = audioCtx.createOscillator();
                let subGain = audioCtx.createGain();
                subOsc.type = 'sine';
                subOsc.frequency.setValueAtTime(160, now);
                subOsc.frequency.exponentialRampToValueAtTime(55, now + 0.3);
                subGain.gain.setValueAtTime(0.5, now); // 볼륨감 대폭 상향
                subGain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
                subOsc.connect(subGain); subGain.connect(audioCtx.destination);
                subOsc.start(now); subOsc.stop(now + 0.3);

                // 2. 발로란트 헤드샷 특유의 쨍하고 웅장한 메탈릭 소리 (Metallic Ringing)
                let ringOsc = audioCtx.createOscillator();
                let ringGain = audioCtx.createGain();
                ringOsc.type = 'triangle';
                ringOsc.frequency.setValueAtTime(1100, now);
                ringOsc.frequency.linearRampToValueAtTime(450, now + 0.2);
                ringGain.gain.setValueAtTime(0.25, now);
                ringGain.gain.exponentialRampToValueAtTime(0.001, now + 0.2);
                ringOsc.connect(ringGain); ringGain.connect(audioCtx.destination);
                ringOsc.start(now); ringOsc.stop(now + 0.2);
            } catch(e) {}
        }

        // ========================================================
        // STAGE 1: 핵심 전역 변수 (난이도 포함)
        // ========================================================
        let mode = 'gridshot'; let difficulty = 1; let isPlaying = false; 
        let score = 0; let timeLeft = 30.0; let totalShots = 0; let hitShots = 0; let playerLives = 2;
        let mouseX = 440, mouseY = 210; let rawMouseX = 440, rawMouseY = 210; let isMouseDown = false;
        let playerX = 440; let playerVx = 0; let keys = { a: false, d: false };
        let showMovingError = false; let errorTimer = 0; let sensitivity = 1.0;
        let projectiles = []; let enemyShootTimer = 0; let showHitEffect = false; let hitEffectTimer = 0;
        let highScores = { gridshot: 0, tracking: 0, microflex: 0, breaking: 0 };
        let targets = [];

        // 난이도별 세부 스펙 가중치
        const diffSpecs = {
            1: { sizeMult: 1.4, speedMult: 0.7 },
            2: { sizeMult: 1.0, speedMult: 1.1 },
            3: { sizeMult: 0.8, speedMult: 1.6 },
            4: { sizeMult: 0.55, speedMult: 2.2 }
        };

        // ========================================================
        // STAGE 2 & 3: 서브 엔진 변수
        // ========================================================
        let isMiniHovered = false; let miniScore = 0; let miniCombo = 0; let miniTargets = [];
        let isRangePlaying = false; let rangeScore = 0; let rangeTimeLeft = 30.0;
        let rangeX = 580; let rangeVx = 0; let rangeBots = []; let rMouseX = 580, rMouseY = 190;
        const rangeUIBox = [
            { id: 'start', x: 440, y: 40, w: 140, h: 30, label: "🤖 START CHALLENGE" },
            { id: 'respawn', x: 600, y: 40, w: 100, h: 30, label: "🤖 RESPAWN" }
        ];

        // --- 컨트롤러 가동 시스템 ---
        function setDifficulty(lvl) {
            if (isPlaying) return;
            difficulty = lvl;
            const colors = { 1: '#22c55e', 2: '#eab308', 3: '#f97316', 4: '#ef4444' };
            for(let i=1; i<=4; i++) {
                const btn = document.getElementById('df-' + i);
                if (i === lvl) { btn.style.background = colors[lvl]; btn.style.color = 'black'; btn.style.border = 'none'; } 
                else { btn.style.background = '#07080b'; btn.style.color = '#e5e7eb'; btn.style.border = '1px solid #374151'; }
            }
            initTargets();
        }

        // 마우스 및 사격 연산 바인딩
        canvas.addEventListener('mousemove', (e) => {
            let rect = canvas.getBoundingClientRect(); rawMouseX = e.clientX - rect.left; rawMouseY = e.clientY - rect.top;
        });
        canvas.addEventListener('mousedown', () => { isMouseDown = true; handleMainClick(); });
        window.addEventListener('mouseup', () => { isMouseDown = false; });

        miniCanvas.addEventListener('mouseenter', () => { isMiniHovered = true; });
        miniCanvas.addEventListener('mouseleave', () => { isMiniHovered = false; miniCombo = 0; });
        miniCanvas.addEventListener('mousedown', (e) => {
            let rect = miniCanvas.getBoundingClientRect(); let mX = e.clientX - rect.left; let mY = e.clientY - rect.top;
            let hit = false;
            for(let i = miniTargets.length - 1; i >= 0; i--) {
                if (Math.hypot(mX - miniTargets[i].x, mY - miniTargets[i].y) <= miniTargets[i].r) {
                    miniScore += 100 + (miniCombo * 10); miniCombo++; hit = true;
                    playGrandKillSound(); miniTargets.splice(i, 1); break;
                }
            }
            if(!hit) { miniCombo = 0; miniScore = Math.max(0, miniScore - 30); }
            document.getElementById('mini-score').innerText = "SCORE: " + miniScore;
            document.getElementById('mini-combo').innerText = "COMBO: " + miniCombo;
        });

        rangeCanvas.addEventListener('mousemove', (e) => {
            let rect = rangeCanvas.getBoundingClientRect(); rMouseX = e.clientX - rect.left; rMouseY = e.clientY - rect.top;
        });
        rangeCanvas.addEventListener('mousedown', () => { handleRangeClick(); });

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

        function handleRangeClick() {
            for(let i=0; i<rangeUIBox.length; i++) {
                let box = rangeUIBox[i];
                if (rMouseX >= box.x && rMouseX <= box.x + box.w && rMouseY >= box.y && rMouseY <= box.y + box.h) {
                    playGrandKillSound();
                    if (box.id === 'start' && !isRangePlaying) { isRangePlaying = true; rangeScore = 0; rangeTimeLeft = 30.0; rangeBots = [generateRangeBotData(), generateRangeBotData()]; }
                    if (box.id === 'respawn') { isRangePlaying = false; rangeBots = []; }
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

        function updateSensitivity(val) { sensitivity = parseFloat(val); document.getElementById('sens-val').innerText = sensitivity.toFixed(2); }
        function changeMode(m) { mode = m; quitSession(); initTargets(); updateDashboard(); }
        function initTargets() { targets = []; let count = (mode === 'gridshot') ? 3 : 1; for(let i=0; i<count; i++) targets.push(generateTargetData()); }
        
        function generateTargetData() {
            let baseRadius = 16; let baseSpeed = 2.8;
            if (mode === 'tracking') { baseRadius = 20; baseSpeed = 4.0; }
            else if (mode === 'microflex') { baseRadius = 10; baseSpeed = 3.5; }
            
            // 난이도 가중치 반영 연산
            let spec = diffSpecs[difficulty];
            return {
                x: 100 + Math.random() * (canvas.width - 200),
                y: 80 + Math.random() * (mode === 'breaking' ? 70 : (canvas.height - 180)),
                radius: baseRadius * spec.sizeMult,
                vx: (Math.random() > 0.5 ? 1 : -1) * (baseSpeed * spec.speedMult),
                vy: (mode === 'breaking') ? 0 : (Math.random() - 0.5) * (baseSpeed * spec.speedMult)
            };
        }

        function generateRangeBotData() { return { x: 120 + Math.random() * (rangeCanvas.width - 240), y: 160 + Math.random() * 120, r: 15, vx: (Math.random() > 0.5 ? 1 : -1) * 2.5 }; }
        function startSession() { isPlaying = true; score = 0; timeLeft = 30.0; totalShots = 0; hitShots = 0; playerLives = 2; projectiles = []; initTargets(); document.getElementById('start-btn').innerText = "⏱ 진행중"; document.getElementById('quit-btn').style.display = "inline-block"; }
        function quitSession() { isPlaying = false; document.getElementById('start-btn').innerText = "▶ 훈련 시작"; document.getElementById('quit-btn').style.display = "none"; projectiles = []; updateDashboard(); }
        function updateDashboard() { document.getElementById('ui-score').innerText = "SCORE: " + score; document.getElementById('ui-acc').innerText = "ACC: " + (totalShots>0?Math.round((hitShots/totalShots)*100):100) + "%"; document.getElementById('ui-time').innerText = "TIME: " + timeLeft.toFixed(1) + "s"; }
        function renderScoresUI() { document.getElementById('record-board').innerHTML = `<div>🎯 GRIDSHOT <span style="color:#38bdf8; font-weight:bold;">${highScores.gridshot}</span></div><div>🔄 TRACKING <span style="color:#00f2fe; font-weight:bold;">${highScores.tracking}</span></div><div>⚡ MICROFLEX <span style="color:#f43f5e; font-weight:bold;">${highScores.microflex}</span></div><div>💥 BREAKING <span style="color:#ff4655; font-weight:bold;">${highScores.breaking}</span></div>`; }

        // --- 초고속 60FPS 하이브리드 루프 엔진 ---
        function loop() {
            // STAGE 1 가동
            if (showHitEffect && hitEffectTimer > 0) { ctx.fillStyle = '#220d11'; hitEffectTimer--; if(hitEffectTimer<=0) showHitEffect=false; } else { ctx.fillStyle = '#090b15'; }
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            if (keys.a) playerVx = Math.max(-5.5, playerVx - 0.8); else if (keys.d) playerVx = Math.min(5.5, playerVx + 0.8); else { playerVx *= 0.6; }
            playerX = Math.max(40, Math.min(canvas.width - 40, playerX + playerVx));
            mouseX = rawMouseX; mouseY = rawMouseY;

            if (isPlaying) {
                timeLeft -= 1/60; if (timeLeft <= 0) { timeLeft = 0; isPlaying = false; if(score>highScores[mode]){highScores[mode]=score; renderScoresUI();} quitSession(); }
                if (mode === 'tracking' && isMouseDown) { targets.forEach(t => { if(Math.hypot(mouseX-t.x, mouseY-t.y)<=t.radius) score+=2; }); }
                
                targets.forEach(t => {
                    t.x += t.vx; t.y += t.vy;
                    if(t.x - t.radius < 10 || t.x + t.radius > canvas.width - 10) t.vx *= -1;
                    if(t.y - t.radius < 10 || t.y + t.radius > canvas.height - 10) t.vy *= -1;
                    ctx.strokeStyle = '#00f2fe'; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI*2); ctx.stroke();
                });
            }
            ctx.fillStyle = Math.abs(playerVx) <= 0.2 ? '#22c55e' : '#eab308'; ctx.fillRect(playerX - 20, canvas.height - 20, 40, 8);
            ctx.fillStyle = '#ff4655'; ctx.beginPath(); ctx.arc(mouseX, mouseY, 3.5, 0, Math.PI*2); ctx.fill();

            // STAGE 2 가동 (자동 미니게임)
            miniCtx.fillStyle = '#070913'; miniCtx.fillRect(0, 0, miniCanvas.width, miniCanvas.height);
            if (isMiniHovered) {
                if (miniTargets.length < 4 && Math.random() < 0.05) miniTargets.push({ x: 30 + Math.random()*(miniCanvas.width-60), y: 30 + Math.random()*(miniCanvas.height-60), r: 0, maxR: 14+Math.random()*10, grow: true });
                for(let i=miniTargets.length-1; i>=0; i--) {
                    let mt = miniTargets[i];
                    if(mt.grow) { mt.r += 0.4; if(mt.r >= mt.maxR) mt.grow = false; } else { mt.r -= 0.25; if(mt.r <= 2) { miniTargets.splice(i, 1); miniCombo = 0; continue; } }
                    miniCtx.fillStyle = 'rgba(168, 85, 247, 0.2)'; miniCtx.beginPath(); miniCtx.arc(mt.x, mt.y, mt.r, 0, Math.PI*2); miniCtx.fill();
                    miniCtx.strokeStyle = '#a855f7'; miniCtx.lineWidth = 1.5; miniCtx.stroke();
                }
            } else {
                miniCtx.fillStyle = '#4b5563'; miniCtx.font = '12px sans-serif'; miniCtx.textAlign = 'center'; miniCtx.fillText("이곳에 마우스를 올리면 과녁이 활성화됩니다.", miniCanvas.width/2, miniCanvas.height/2);
            }

            // STAGE 3 가동 (발로란트 사격장)
            rangeCtx.fillStyle = '#0b0e14'; rangeCtx.fillRect(0, 0, rangeCanvas.width, rangeCanvas.height);
            rangeUIBox.forEach(box => {
                rangeCtx.fillStyle = box.id === 'start' ? (isRangePlaying ? '#374151' : '#047857') : '#b91c1c'; rangeCtx.fillRect(box.x, box.y, box.w, box.h);
                rangeCtx.fillStyle = '#ffffff'; rangeCtx.font = 'bold 11px sans-serif'; rangeCtx.textAlign = 'center'; rangeCtx.fillText(box.label, box.x + box.w/2, box.y + box.h/1.6);
            });
            rangeCtx.fillStyle = '#e5e7eb'; rangeCtx.font = 'bold 14px monospace'; rangeCtx.fillText(`[THE RANGE] SCORE: ${rangeScore} | TIME: ${rangeTimeLeft.toFixed(1)}s`, 40, 60);

            if (isRangePlaying) {
                rangeTimeLeft -= 1/60; if(rangeTimeLeft <= 0) isRangePlaying = false;
                rangeBots.forEach(b => {
                    b.x += b.vx; if(b.x - b.r < 20 || b.x + b.r > rangeCanvas.width - 20) b.vx *= -1;
                    rangeCtx.fillStyle = '#ff4655'; rangeCtx.beginPath(); rangeCtx.arc(b.x, b.y, b.r, 0, Math.PI*2); rangeCtx.fill();
                });
            }
            rangeCtx.strokeStyle = '#ff4655'; rangeCtx.lineWidth = 1.5; rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX-6, rMouseY); rangeCtx.lineTo(rMouseX+6, rMouseY); rangeCtx.stroke();
            rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX, rMouseY-6); rangeCtx.lineTo(rMouseX, rMouseY+6); rangeCtx.stroke();

            window.requestAnimationFrame(loop);
        }

        renderScoresUI(); initTargets(); loop();
    </script>
    """
    st.components.v1.html(html_src, height=1280)

if __name__ == "__main__":
    main()
