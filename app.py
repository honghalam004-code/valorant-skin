import streamlit as st

def main():
    st.set_page_config(page_title="AIMLAB + VALORANT RANGE", layout="wide")

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

    st.markdown("<h1 style='text-align:center; color:#ff4655; font-weight:900;'>🎯 AIM TRAINING ULTIMATE SYSTEM</h1>", unsafe_allow_html=True)

    html_src = """
    <div style="max-width:1200px; margin:0 auto; display:flex; flex-direction:column; gap:35px;">
        
        <h3 class="section-title" style="color:#00f2fe; border-color:#00f2fe;">STAGE 01 : MAIN AIMLAB (4대 모드 완전 가동)</h3>
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
                    <div style="color:#ff4655; font-size:11px; font-weight:bold; margin-bottom:6px;">⚙️ MOUSE SENSITIVITY</div>
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
                    <div style="color:#00f2fe; font-size:11px; font-weight:bold; margin-bottom:8px;">💡 현재 모드 가이드</div>
                    <div style="font-size:12px; color:#9ca3af; line-height:1.6;" id="mode-tip">
                        <b>GRIDSHOT:</b> 3개의 과녁을 빠르게 파괴하세요.
                    </div>
                </div>
            </div>
        </div>

        <h3 class="section-title" style="color:#a855f7; border-color:#a855f7;">STAGE 02 : EASY AIM POP (손풀기 미니게임)</h3>
        <div style="background:#111625; padding:20px; border-radius:8px; border:1px solid #1f2942; display:flex; gap:25px; align-items:center;">
            <div style="flex:1;">
                <p style="margin:0 0 10px 0; color:#e5e7eb; font-size:14px; font-weight:bold;">💡 마우스만 올리면 가동되는 편안한 서프 에임 판</p>
                <p style="margin:0 0 15px 0; color:#9ca3af; font-size:12px; line-height:1.5;">수축 속도를 완화하여 조준선을 편안하게 옮겨 타격하기 좋습니다. 인공음이 완전히 배제되었습니다.</p>
                <div style="display:flex; gap:15px; font-family:monospace; font-size:14px; font-weight:bold; background:#070913; padding:12px; border-radius:6px; border:1px solid #1f2942;">
                    <div style="color:#a855f7;" id="mini-score">SCORE: 0</div>
                    <div style="color:#34d399;" id="mini-combo">COMBO: 0</div>
                </div>
            </div>
            <canvas id="miniCanvas" width="620" height="200" style="background:#070913; border:2px dashed #a855f7; border-radius:6px; cursor:crosshair;"></canvas>
        </div>

        <h3 class="section-title" style="color:#ff4655; border-color:#ff4655;">STAGE 03 : VALORANT THE RANGE (사격 연습장 무제한 모드)</h3>
        <div style="background:#111625; padding:15px; border-radius:8px; border:1px solid #1f2942; text-align:center;">
            <p style="margin:0 0 10px 0; color:#9ca3af; font-size:12px;">🎯 움직이면서 쏘면 <b>에임오차(탄퍼짐)</b>가 발생합니다! <b>A/D 키 무빙 후 브레이킹을 걸고 정지 상태에서 헤드</b>를 노리세요.</p>
            <canvas id="rangeCanvas" width="1160" height="400" style="background:#0e111a; border:2px solid #ff4655; border-radius:6px; cursor:none;"></canvas>
        </div>

    </div>

    <script>
        const canvas = document.getElementById('aimCanvas'); const ctx = canvas.getContext('2d');
        const miniCanvas = document.getElementById('miniCanvas'); const miniCtx = miniCanvas.getContext('2d');
        const rangeCanvas = document.getElementById('rangeCanvas'); const rangeCtx = rangeCanvas.getContext('2d');

        // --- 🎵 리얼 타격 숏 오디오 엔진 (네트워크 다운로드 및 가짜 기계음 완벽 제거) ---
        let audioCtx = null;
        function playValorantKillSound() {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();

                // 인공 비프음을 완전히 차단하기 위해 원음 0.04초짜리 리얼 화이트노이즈 스냅 버스트 버퍼 생성
                let bufferSize = audioCtx.sampleRate * 0.04;
                let buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
                let data = buffer.getChannelData(0);
                
                // 귀에 거슬리는 인공적인 사인파를 지우고 타격 질감용 타임 노이즈 주입
                for (let i = 0; i < bufferSize; i++) {
                    data[i] = Math.random() * 2 - 1;
                }

                let noiseNode = audioCtx.createBufferSource();
                noiseNode.buffer = buffer;

                // 타격의 둔탁함과 청량함을 잡는 로우패스/하이패스 직렬 필터 레이어 구성
                let lpFilter = audioCtx.createBiquadFilter();
                lpFilter.type = 'lowpass';
                lpFilter.frequency.setValueAtTime(1000, audioCtx.currentTime);

                let hpFilter = audioCtx.createBiquadFilter();
                hpFilter.type = 'highpass';
                hpFilter.frequency.setValueAtTime(150, audioCtx.currentTime);

                let gainNode = audioCtx.createGain();
                gainNode.gain.setValueAtTime(0.35, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.04);

                noiseNode.connect(lpFilter);
                lpFilter.connect(hpFilter);
                hpFilter.connect(gainNode);
                gainNode.connect(audioCtx.destination);

                noiseNode.start();
            } catch(e) { console.log(e); }
        }

        // ========================================================
        // STAGE 1 전역 기믹 설계부
        // ========================================================
        let mode = 'gridshot'; let difficulty = 1; let isPlaying = false; 
        let score = 0; let timeLeft = 30.0; let totalShots = 0; let hitShots = 0;
        let mouseX = 440, mouseY = 210; let rawMouseX = 440, rawMouseY = 210; let isMouseDown = false;
        let playerX = 440; let playerVx = 0; let keys = { a: false, d: false };
        let showMovingError = false; let errorTimer = 0; let sensitivity = 1.0;
        let targets = [];

        const diffSpecs = {
            1: { sizeMult: 1.4, speedMult: 0.7 },
            2: { sizeMult: 1.0, speedMult: 1.0 },
            3: { sizeMult: 0.75, speedMult: 1.5 },
            4: { sizeMult: 0.5, speedMult: 2.1 }
        };

        // ========================================================
        // STAGE 2 & STAGE 3 (발로란트 연습장) 설계부
        // ========================================================
        let isMiniHovered = false; let miniScore = 0; let miniCombo = 0; let miniTargets = [];
        
        let isRangePlaying = false; let rangeScore = 0;
        let rangePlayerX = 580; let rangePlayerVx = 0; 
        let rangeBots = []; let rMouseX = 580, rMouseY = 200;
        
        const rangeUIBox = [
            { id: 'start', x: 440, y: 35, w: 120, h: 35, label: "🤖 START" },
            { id: 'clear', x: 580, y: 35, w: 120, h: 35, label: "🧹 CLEAR" }
        ];

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

        function changeMode(m) {
            mode = m; quitSession(); initTargets();
            const tipEl = document.getElementById('mode-tip');
            if(m === 'gridshot') tipEl.innerHTML = "<b>GRIDSHOT:</b> 전방의 과녁 3개를 빠르게 제거하는 플릭 훈련장입니다.";
            else if(m === 'tracking') tipEl.innerHTML = "<b>TRACKING:</b> 마우스를 누른 상태로 이동하는 표적 위에 조준선을 유지하세요.";
            else if(m === 'microflex') tipEl.innerHTML = "<b>MICROFLEX:</b> 좁은 범위에서 짧게 스폰되는 작은 표적을 소멸 전에 맞추세요.";
            else if(m === 'breaking') tipEl.innerHTML = "<b>VAL-BREAKING:</b> 좌우 이동 후 완전히 정지하여 녹색 불이 들어오는 타이밍에 정밀 사격하세요.";
            
            ['grid', 'track', 'micro', 'break'].forEach(k => {
                const el = document.getElementById('m-' + k);
                let targetKey = m.substring(0,5); if (m === 'breaking') targetKey = 'break';
                if (k === targetKey) { el.style.background = m === 'breaking' ? '#ff4655' : '#00f2fe'; el.style.color = 'black'; el.style.border = 'none'; } 
                else { el.style.background = '#07080b'; el.style.color = k === 'break' ? '#ff4655' : '#00f2fe'; el.style.border = '1px solid currentColor'; }
            });
        }

        window.addEventListener('keydown', (e) => {
            if (e.key.toLowerCase() === 'a') keys.a = true; if (e.key.toLowerCase() === 'd') keys.d = true;
        });
        window.addEventListener('keyup', (e) => {
            if (e.key.toLowerCase() === 'a') keys.a = false; if (e.key.toLowerCase() === 'd') keys.d = false;
        });

        canvas.addEventListener('mousemove', (e) => { let rect = canvas.getBoundingClientRect(); rawMouseX = e.clientX - rect.left; rawMouseY = e.clientY - rect.top; });
        canvas.addEventListener('mousedown', () => { isMouseDown = true; handleMainClick(); });
        window.addEventListener('mouseup', () => { isMouseDown = false; });

        miniCanvas.addEventListener('mouseenter', () => { isMiniHovered = true; });
        miniCanvas.addEventListener('mouseleave', () => { isMiniHovered = false; miniCombo = 0; });
        miniCanvas.addEventListener('mousedown', (e) => {
            let rect = miniCanvas.getBoundingClientRect(); let mX = e.clientX - rect.left; let mY = e.clientY - rect.top;
            let hit = false;
            for(let i = miniTargets.length - 1; i >= 0; i--) {
                if (Math.hypot(mX - miniTargets[i].x, mY - miniTargets[i].y) <= miniTargets[i].r) {
                    miniScore += 100; miniCombo++; hit = true; playValorantKillSound(); miniTargets.splice(i, 1); break;
                }
            }
            if(!hit) { miniCombo = 0; miniScore = Math.max(0, miniScore - 20); }
            document.getElementById('mini-score').innerText = "SCORE: " + miniScore;
            document.getElementById('mini-combo').innerText = "COMBO: " + miniCombo;
        });

        rangeCanvas.addEventListener('mousemove', (e) => { let rect = rangeCanvas.getBoundingClientRect(); rMouseX = e.clientX - rect.left; rMouseY = e.clientY - rect.top; });
        rangeCanvas.addEventListener('mousedown', () => { handleRangeClick(); });

        function handleMainClick() {
            if (!isPlaying || mode === 'tracking') return;
            totalShots++; let hitAny = false;
            for (let i = 0; i < targets.length; i++) {
                let t = targets[i];
                if (Math.hypot(mouseX - t.x, mouseY - t.y) <= t.radius) {
                    if (mode === 'breaking' && Math.abs(playerVx) > 0.15) {
                        score = Math.max(0, score - 50); showMovingError = true; errorTimer = 25; return;
                    }
                    hitShots++; score += 100; hitAny = true;
                    playValorantKillSound(); targets[i] = generateTargetData(); break;
                }
            }
            if (!hitAny) score = Math.max(0, score - 20); updateDashboard();
        }

        function handleRangeClick() {
            for(let i=0; i<rangeUIBox.length; i++) {
                let box = rangeUIBox[i];
                if (rMouseX >= box.x && rMouseX <= box.x + box.w && rMouseY >= box.y && rMouseY <= box.y + box.h) {
                    playValorantKillSound();
                    if (box.id === 'start' && !isRangePlaying) { isRangePlaying = true; rangeScore = 0; spawnRangeBot(); }
                    if (box.id === 'clear') { isRangePlaying = false; rangeBots = []; }
                    return;
                }
            }
            if (!isRangePlaying) return;

            let spreadMult = Math.abs(rangePlayerVx) * 3.5;
            let finalMouseX = rMouseX + (Math.random() - 0.5) * spreadMult;
            let finalMouseY = rMouseY + (Math.random() - 0.5) * spreadMult;

            let hit = false;
            for(let i = rangeBots.length - 1; i >= 0; i--) {
                let b = rangeBots[i];
                if (Math.hypot(finalMouseX - b.x, finalMouseY - b.headY) <= b.headR) {
                    rangeScore += 100; hit = true; playValorantKillSound();
                    rangeBots.splice(i, 1); spawnRangeBot(); break;
                }
            }
        }

        function initTargets() { targets = []; let count = (mode === 'gridshot') ? 3 : 1; for(let i=0; i<count; i++) targets.push(generateTargetData()); }
        function generateTargetData() {
            let spec = diffSpecs[difficulty];
            let baseRadius = 16 * spec.sizeMult; let baseSpeed = 2.5 * spec.speedMult;
            if (mode === 'tracking') return { x: 440, y: 210, radius: 22 * spec.sizeMult, angle: Math.random() * Math.PI * 2, speed: baseSpeed * 1.2 };
            if (mode === 'microflex') return { x: 300 + Math.random() * 280, y: 140 + Math.random() * 140, radius: 10 * spec.sizeMult, life: 75, maxLife: 75 };
            if (mode === 'breaking') return { x: 150 + Math.random() * 580, y: 240, radius: 16 * spec.sizeMult, vx: (Math.random() > 0.5 ? 1 : -1) * baseSpeed, vy: 0 };
            return { x: 120 + Math.random() * 640, y: 80 + Math.random() * 240, radius: baseRadius, vx: 0, vy: 0 };
        }

        function spawnRangeBot() {
            rangeBots = [{
                x: 350 + Math.random() * 460,
                y: 220,
                bodyW: 24, bodyH: 45,
                headY: 195, headR: 10,
                vx: (Math.random() > 0.5 ? 1 : -1) * 1.6
            }];
        }

        function updateSensitivity(val) { sensitivity = parseFloat(val); document.getElementById('sens-val').innerText = sensitivity.toFixed(2); }
        function startSession() { isPlaying = true; score = 0; timeLeft = 30.0; totalShots = 0; hitShots = 0; initTargets(); document.getElementById('start-btn').innerText = "⏱ 진행중"; document.getElementById('quit-btn').style.display = "inline-block"; }
        function quitSession() { isPlaying = false; document.getElementById('start-btn').innerText = "▶ 훈련 시작"; document.getElementById('quit-btn').style.display = "none"; updateDashboard(); }
        function updateDashboard() { document.getElementById('ui-score').innerText = "SCORE: " + score; document.getElementById('ui-acc').innerText = "ACC: " + (totalShots>0?Math.round((hitShots/totalShots)*100):100) + "%"; document.getElementById('ui-time').innerText = "TIME: " + timeLeft.toFixed(1) + "s"; }

        // ========================================================
        // 🔄 통합 초고속 루프 코어 엔진
        // ========================================================
        function loop() {
            // STAGE 1 가동 연산
            ctx.fillStyle = '#090b15'; ctx.fillRect(0, 0, canvas.width, canvas.height);
            if (keys.a) playerVx = Math.max(-5.0, playerVx - 0.7); else if (keys.d) playerVx = Math.min(5.0, playerVx + 0.7); else { playerVx *= 0.65; }
            playerX = Math.max(40, Math.min(canvas.width - 40, playerX + playerVx)); mouseX = rawMouseX; mouseY = rawMouseY;

            if (isPlaying) {
                timeLeft -= 1/60; if (timeLeft <= 0) { timeLeft = 0; quitSession(); }
                if (mode === 'tracking') {
                    let t = targets[0]; t.angle += 0.03 * t.speed; t.x += Math.cos(t.angle) * t.speed; t.y += Math.sin(t.angle) * (t.speed * 0.5);
                    if(t.x < 50 || t.x > canvas.width - 50) t.angle = Math.PI - t.angle; if(t.y < 50 || t.y > canvas.height - 120) t.angle = -t.angle;
                    if (isMouseDown && Math.hypot(mouseX - t.x, mouseY - t.y) <= t.radius) { score += 3; updateDashboard(); if(Math.random()<0.08) playValorantKillSound(); }
                    ctx.fillStyle = 'rgba(0, 242, 254, 0.15)'; ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI*2); ctx.fill();
                    ctx.strokeStyle = '#00f2fe'; ctx.lineWidth = 2.5; ctx.stroke();
                } else if (mode === 'microflex') {
                    let t = targets[0]; t.life--; if(t.life <= 0) targets[0] = generateTargetData();
                    ctx.fillStyle = '#22c55e'; ctx.fillRect(t.x - t.radius, t.y - t.radius - 8, (t.radius * 2) * (t.life / t.maxLife), 3);
                    ctx.strokeStyle = '#f43f5e'; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI*2); ctx.stroke();
                } else {
                    targets.forEach(t => { t.x += (t.vx || 0); if(t.x - t.radius < 20 || t.x + t.radius > canvas.width - 20) t.vx *= -1; ctx.strokeStyle = mode==='breaking'?'#ff4655':'#38bdf8'; ctx.lineWidth = 2.5; ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI*2); ctx.stroke(); });
                }
            }
            ctx.fillStyle = Math.abs(playerVx) <= 0.15 ? '#22c55e' : '#eab308'; ctx.fillRect(playerX - 20, canvas.height - 15, 40, 6);
            if (showMovingError && errorTimer > 0) { ctx.fillStyle = '#ff4655'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'center'; ctx.fillText("❌ 브레이킹 미체결 (정지 상태에서 사격하세요)", canvas.width/2, 60); errorTimer--; if(errorTimer <= 0) showMovingError = false; }
            ctx.fillStyle = '#ff4655'; ctx.beginPath(); ctx.arc(mouseX, mouseY, 3.5, 0, Math.PI*2); ctx.fill();


            // STAGE 2 가동 연산
            miniCtx.fillStyle = '#070913'; miniCtx.fillRect(0, 0, miniCanvas.width, miniCanvas.height);
            if (isMiniHovered) {
                if (miniTargets.length < 3 && Math.random() < 0.03) miniTargets.push({ x: 40 + Math.random()*(miniCanvas.width-80), y: 40 + Math.random()*(miniCanvas.height-80), r: 0, maxR: 16+Math.random()*8, grow: true });
                for(let i=miniTargets.length-1; i>=0; i--) {
                    let mt = miniTargets[i]; if(mt.grow) { mt.r += 0.25; if(mt.r >= mt.maxR) mt.grow = false; } else { mt.r -= 0.15; if(mt.r <= 2) { miniTargets.splice(i, 1); miniCombo = 0; continue; } }
                    miniCtx.fillStyle = 'rgba(168, 85, 247, 0.2)'; miniCtx.beginPath(); miniCtx.arc(mt.x, mt.y, mt.r, 0, Math.PI*2); miniCtx.fill();
                    miniCtx.strokeStyle = '#a855f7'; miniCtx.lineWidth = 1.5; miniCtx.stroke();
                }
            } else { miniCtx.fillStyle = '#4b5563'; miniCtx.font = '12px sans-serif'; miniCtx.textAlign = 'center'; miniCtx.fillText("이곳에 커서를 가져오면 손풀기 타겟이 개방됩니다.", miniCanvas.width/2, miniCanvas.height/2); }


            // STAGE 3 가동 연산 (★ 무제한 사격 연습장)
            rangeCtx.fillStyle = '#0b0f19'; rangeCtx.fillRect(0, 0, rangeCanvas.width, rangeCanvas.height);
            rangeCtx.fillStyle = '#1e293b'; rangeCtx.fillRect(250, 260, 660, 8); // 스폰 플랫폼 베이스라인
            
            // 전광판 컨트롤 스위치
            rangeUIBox.forEach(box => {
                rangeCtx.fillStyle = box.id === 'start' ? (isRangePlaying ? '#1e293b' : '#0f766e') : '#991b1b'; rangeCtx.fillRect(box.x, box.y, box.w, box.h);
                rangeCtx.fillStyle = '#ffffff'; rangeCtx.font = 'bold 11px sans-serif'; rangeCtx.textAlign = 'center'; rangeCtx.fillText(box.label, box.x + box.w/2, box.y + box.h/1.6);
            });

            // 스탯 대시보드
            rangeCtx.fillStyle = '#94a3b8'; rangeCtx.font = 'bold 13px monospace'; rangeCtx.textAlign = 'left';
            rangeCtx.fillText(`[THE RANGE LIVE] HEADSHOT_SCORE: ${rangeScore} | MODE: INFINITE TRAINING`, 45, 55);

            if (keys.a) rangePlayerVx = Math.max(-4.5, rangePlayerVx - 0.6); else if (keys.d) rangePlayerVx = Math.min(4.5, rangePlayerVx + 0.6); else { rangePlayerVx *= 0.65; }
            rangePlayerX = Math.max(100, Math.min(rangeCanvas.width - 100, rangePlayerX + rangePlayerVx));

            if (isRangePlaying) {
                // 상시 스폰 동기화 보장 레이어
                if (rangeBots.length === 0) spawnRangeBot();

                rangeBots.forEach(b => {
                    b.x += b.vx; if(b.x < 300 || b.x > 860) b.vx *= -1;
                    rangeCtx.fillStyle = '#334155'; rangeCtx.fillRect(b.x - b.bodyW/2, b.y, b.bodyW, b.bodyH); // 몸통
                    
                    let hGrad = rangeCtx.createRadialGradient(b.x, b.headY, 2, b.x, b.headY, b.headR);
                    hGrad.addColorStop(0, '#ffffff'); hGrad.addColorStop(1, '#ff4655');
                    rangeCtx.fillStyle = hGrad; rangeCtx.beginPath(); rangeCtx.arc(b.x, b.headY, b.headR, 0, Math.PI*2); rangeCtx.fill(); // 머리
                    rangeCtx.strokeStyle = '#ffffff'; rangeCtx.lineWidth = 1; rangeCtx.stroke();
                });
            }

            // 하단 조작 패드 지시선
            rangeCtx.fillStyle = '#38bdf8'; rangeCtx.fillRect(rangePlayerX - 20, rangeCanvas.height - 15, 40, 5);

            // 무빙 가변 크로스헤어
            let spreadOffset = Math.abs(rangePlayerVx) * 3.5;
            rangeCtx.strokeStyle = Math.abs(rangePlayerVx) <= 0.15 ? '#22c55e' : '#f59e0b'; rangeCtx.lineWidth = 1.8;
            rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX - 5 - spreadOffset, rMouseY); rangeCtx.lineTo(rMouseX - 1 - spreadOffset, rMouseY); rangeCtx.stroke();
            rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX + 1 + spreadOffset, rMouseY); rangeCtx.lineTo(rMouseX + 5 + spreadOffset, rMouseY); rangeCtx.stroke();
            rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX, rMouseY - 5 - spreadOffset); rangeCtx.lineTo(rMouseX, rMouseY - 1 - spreadOffset); rangeCtx.stroke();
            rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX, rMouseY + 1 + spreadOffset); rangeCtx.lineTo(rMouseX, rMouseY + 5 + spreadOffset); rangeCtx.stroke();

            window.requestAnimationFrame(loop);
        }

        initTargets(); loop();
    </script>
    """
    st.components.v1.html(html_src, height=1300)

if __name__ == "__main__":
    main()
