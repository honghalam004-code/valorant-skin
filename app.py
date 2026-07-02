import streamlit as st

def main():
    st.set_page_config(page_title="VALORANT RANGE + AIMLAB CENTER", layout="wide")

    st.markdown("""
        <style>
        .main { background-color: #070913; color: #e5e7eb; font-family: 'Segoe UI', monospace; }
        iframe { border: none !important; }
        .section-title {
            color: #00f2fe; font-weight: 900; letter-spacing: 2px; 
            border-bottom: 2px solid #1f2942; padding-bottom: 6px; margin-top: 10px; margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    html_src = """
    <div style="max-width:1200px; margin:0 auto; display:flex; flex-direction:column; gap:20px; font-family:sans-serif;">
        
        <h3 class="section-title">STAGE 01 : MAIN AIMLAB ENGINE (기본 메인 모드)</h3>
        <div style="display:flex; gap:20px; justify-content:center; align-items:flex-start;">
            <div style="flex: 1; text-align:center;">
                <div style="display:flex; justify-content:space-between; align-items:center; background:#111625; padding:10px 15px; border-radius:6px; margin-bottom:10px; border:1px solid #1f2942;">
                    <div style="display:flex; gap:6px;">
                        <button onclick="changeMode('gridshot')" id="m-grid" style="background:#00f2fe; color:black; border:none; padding:6px 12px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">🎯 GRIDSHOT</button>
                        <button onclick="changeMode('tracking')" id="m-track" style="background:#07080b; color:#00f2fe; border:1px solid #00f2fe; padding:6px 12px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">🔄 TRACKING</button>
                        <button onclick="changeMode('microflex')" id="m-micro" style="background:#07080b; color:#00f2fe; border:1px solid #00f2fe; padding:6px 12px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">⚡ MICROFLEX</button>
                        <button onclick="changeMode('breaking')" id="m-break" style="background:#07080b; color:#ff4655; border:1px solid #ff4655; padding:6px 12px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">⚡ VAL-BREAKING</button>
                    </div>
                    <div style="display:flex; gap:15px; font-family:monospace; font-size:14px; font-weight:bold; align-items:center;">
                        <div style="color:#00f2fe;" id="ui-score">SCORE: 0</div>
                        <div style="color:#34d399;" id="ui-acc">ACC: 100%</div>
                        <div style="color:#f87171;" id="ui-time">TIME: 30.0s</div>
                    </div>
                    <div style="display:flex; gap:6px;">
                        <button onclick="quitSession()" id="quit-btn" style="background:#ef4444; color:white; border:none; padding:6px 12px; font-weight:bold; cursor:pointer; border-radius:4px; display:none;">🚪 나가기</button>
                        <button onclick="startSession()" id="start-btn" style="background:#34d399; color:black; border:none; padding:6px 16px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:12px;">▶ 훈련 시작</button>
                    </div>
                </div>
                <canvas id="aimCanvas" width="890" height="360" style="background:#090b15; border:2px solid #1f2942; border-radius:6px; cursor:none;"></canvas>
            </div>

            <div style="width:250px; display:flex; flex-direction:column; gap:10px;">
                <div style="background:#111625; padding:12px; border-radius:6px; border:1px solid #1f2942;">
                    <div style="color:#ff4655; font-size:11px; font-weight:bold; margin-bottom:4px;">⚙️ MOUSE SENSITIVITY (전체 공통 적용)</div>
                    <input type="range" id="sens-slider" min="0.1" max="4.0" step="0.05" value="1.0" oninput="updateSensitivity(this.value)" style="width:100%; accent-color:#ff4655;">
                    <div style="text-align:right; font-size:13px; font-weight:bold; color:#ff4655; margin-top:2px;" id="sens-val">1.00</div>
                </div>
                
                <div style="background:#111625; padding:12px; border-radius:6px; border:1px solid #1f2942;">
                    <div style="color:#eab308; font-size:12px; font-weight:bold; margin-bottom:6px;">🏆 GLOBAL LEADERBOARD</div>
                    <div style="font-size:12px; font-family:monospace; display:flex; flex-direction:column; gap:4px; color:#cbd5e1;">
                        <div>1위. TENZ - <span style="color:#eab308;">12,500</span></div>
                        <div>2위. ASPAS - <span style="color:#94a3b8;">11,200</span></div>
                        <div>3위. YOU(MY BEST) - <span style="color:#cd7f32;" id="user-best">0</span></div>
                    </div>
                </div>

                <div style="background:#111625; padding:12px; border-radius:6px; border:1px solid #1f2942;">
                    <div style="color:#00f2fe; font-size:11px; font-weight:bold; margin-bottom:6px;">📊 난이도 레벨 설정</div>
                    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:4px;">
                        <button onclick="setDifficulty(1)" id="df-1" style="background:#22c55e; color:black; border:none; padding:6px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:11px;">레벨 1</button>
                        <button onclick="setDifficulty(2)" id="df-2" style="background:#07080b; color:#e5e7eb; border:1px solid #374151; padding:6px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:11px;">레벨 2</button>
                        <button onclick="setDifficulty(3)" id="df-3" style="background:#07080b; color:#e5e7eb; border:1px solid #374151; padding:6px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:11px;">레벨 3</button>
                        <button onclick="setDifficulty(4)" id="df-4" style="background:#07080b; color:#e5e7eb; border:1px solid #374151; padding:6px; font-weight:bold; cursor:pointer; border-radius:4px; font-size:11px;">레벨 4</button>
                    </div>
                </div>
            </div>
        </div>

        <div style="display:flex; gap:20px; width:100%;">
            
            <div style="flex: 1; background:#111625; padding:12px; border-radius:8px; border:1px solid #1f2942;">
                <h4 style="margin:0 0 6px 0; color:#a855f7; font-size:13px; font-weight:900;">STAGE 02 : EASY AIM POP (🟢 RGX 쫀득한 찰진 손맛)</h4>
                <div style="display:flex; gap:10px; font-family:monospace; font-size:12px; font-weight:bold; margin-bottom:8px;">
                    <div style="color:#a855f7;" id="mini-score">SCORE: 0</div>
                    <div style="color:#34d399;" id="mini-combo">COMBO: 0</div>
                </div>
                <canvas id="miniCanvas" width="550" height="200" style="background:#070913; border:2px dashed #a855f7; border-radius:6px; cursor:none; width:100%;"></canvas>
            </div>

            <div style="flex: 1; background:#111625; padding:12px; border-radius:8px; border:1px solid #1f2942;">
                <h4 style="margin:0 0 6px 0; color:#ff4655; font-size:13px; font-weight:900;">STAGE 03 : VALORANT THE RANGE (🎯 와이드 봇 라인 연습장)</h4>
                <div style="display:flex; gap:12px; font-family:monospace; font-size:12px; font-weight:bold; margin-bottom:8px;">
                    <div style="color:#ff4655;" id="range-dashboard">[THE RANGE] HEADSHOTS: 0</div>
                    <div style="color:#38bdf8; font-size:11px; font-weight:normal;">*인게임 싱크: 정면 넓은 라인에 봇들이 리얼하게 늘어서 배치됩니다.</div>
                </div>
                <canvas id="rangeCanvas" width="550" height="200" style="background:#090c14; border:2px solid #ff4655; border-radius:6px; cursor:none; width:100%;"></canvas>
            </div>

        </div>

    </div>

    <script>
        const canvas = document.getElementById('aimCanvas'); const ctx = canvas.getContext('2d');
        const miniCanvas = document.getElementById('miniCanvas'); const miniCtx = miniCanvas.getContext('2d');
        const rangeCanvas = document.getElementById('rangeCanvas'); const rangeCtx = rangeCanvas.getContext('2d');

        // --- 🟢 [RGX REAL TIGHT MIX] 깡통 소리 삭제, 쫀득하고 찰지게 감기는 타격 오디오 엔진 ---
        let audioCtx = null;

        function playRGXSound() {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();

                let now = audioCtx.currentTime;

                // 1. 💥 촥 감기는 질감의 로우/미드 베이스 타격 (Tight Squash Hit)
                // 로우 패스 노이즈와 커스텀 오실레이터를 묶어 깡통 소리를 지우고 끈적하고 단단한 밀도감을 줌
                let bufferSize = audioCtx.sampleRate * 0.04;
                let noiseBuffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
                let noiseData = noiseBuffer.getChannelData(0);
                for (let i = 0; i < bufferSize; i++) {
                    noiseData[i] = (Math.random() * 2 - 1) * Math.exp(-60 * (i / audioCtx.sampleRate));
                }
                let noiseSource = audioCtx.createBufferSource();
                noiseSource.buffer = noiseBuffer;

                let noiseFilter = audioCtx.createBiquadFilter();
                noiseFilter.type = 'lowpass';
                noiseFilter.frequency.setValueAtTime(350, now); // 먹먹하고 단단하게 가둠

                let noiseGain = audioCtx.createGain();
                noiseGain.gain.setValueAtTime(1.2, now);
                noiseGain.gain.exponentialRampToValueAtTime(0.001, now + 0.035);

                noiseSource.connect(noiseFilter);
                noiseFilter.connect(noiseGain);
                noiseGain.connect(audioCtx.destination);

                // 2. ⚡ RGX 고유의 쫀득한 메탈릭 전자 파형 코어 (Cyber Elastic Snap)
                let osc = audioCtx.createOscillator();
                let oscGain = audioCtx.createGain();
                
                osc.type = 'triangle'; // 부드럽고 묵직한 배음
                osc.frequency.setValueAtTime(580, now);
                // 주파수를 순간적으로 아래로 강하게 떨어뜨려 "촥-" 하고 달라붙는 쫀득한 청각적 탄성을 유도
                osc.frequency.exponentialRampToValueAtTime(80, now + 0.03); 

                oscGain.gain.setValueAtTime(0.9, now);
                oscGain.gain.exponentialRampToValueAtTime(0.001, now + 0.04); // 아주 정밀하고 타이트하게 끊어침

                osc.connect(oscGain);
                oscGain.connect(audioCtx.destination);

                // 3. 🔌 특유의 하이테크 레이저 잔향음 (Subtle Magnetic Tail)
                let tailOsc = audioCtx.createOscillator();
                let tailGain = audioCtx.createGain();
                tailOsc.type = 'sine';
                tailOsc.frequency.setValueAtTime(720, now);

                tailGain.gain.setValueAtTime(0.18, now);
                tailGain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);

                tailOsc.connect(tailGain);
                tailGain.connect(audioCtx.destination);

                noiseSource.start(now);
                osc.start(now);
                tailOsc.start(now);

                osc.stop(now + 0.05);
                tailOsc.stop(now + 0.16);

            } catch(e) { console.log(e); }
        }

        // ========================================================
        // ⚙️ 전역 변수 관리부
        // ========================================================
        let mode = 'gridshot'; let difficulty = 1; let isPlaying = false; 
        let score = 0; let timeLeft = 30.0; let totalShots = 0; let hitShots = 0; let userBestScore = 0;
        
        let mouseX = 445, mouseY = 180; 
        let miniMouseX = 275, miniMouseY = 100;
        let rMouseX = 275, rMouseY = 100;
        
        let isMouseDown = false;
        let playerX = 445; let playerVx = 0; let keys = { a: false, d: false };
        let showMovingError = false; let errorTimer = 0; 
        let sensitivity = 1.0; 
        let targets = [];

        const diffSpecs = {
            1: { sizeMult: 1.4, speedMult: 0.7 },
            2: { sizeMult: 1.0, speedMult: 1.0 },
            3: { sizeMult: 0.75, speedMult: 1.5 },
            4: { sizeMult: 0.5, speedMult: 2.1 }
        };

        let isMiniHovered = false; let miniScore = 0; let miniCombo = 0; let miniTargets = [];
        let isRangePlaying = false; let rangeScore = 0;
        let rangePlayerX = 275; let rangePlayerVx = 0; 
        let rangeBots = [];
        
        const rangeUIBox = [
            { id: 'start', x: 180, y: 15, w: 90, h: 25, label: "🤖 START" },
            { id: 'clear', x: 280, y: 15, w: 90, h: 25, label: "🧹 CLEAR" }
        ];

        function updateSensitivity(val) { 
            sensitivity = parseFloat(val); 
            document.getElementById('sens-val').innerText = sensitivity.toFixed(2); 
        }

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

        canvas.addEventListener('mousemove', (e) => { 
            let rect = canvas.getBoundingClientRect(); 
            let targetX = e.clientX - rect.left; let targetY = e.clientY - rect.top;
            mouseX += (targetX - mouseX) * sensitivity; mouseY += (targetY - mouseY) * sensitivity;
            mouseX = Math.max(0, Math.min(canvas.width, mouseX)); mouseY = Math.max(0, Math.min(canvas.height, mouseY));
        });
        canvas.addEventListener('mousedown', () => { isMouseDown = true; handleMainClick(); });
        window.addEventListener('mouseup', () => { isMouseDown = false; });

        miniCanvas.addEventListener('mouseenter', () => { isMiniHovered = true; });
        miniCanvas.addEventListener('mouseleave', () => { isMiniHovered = false; miniCombo = 0; });
        miniCanvas.addEventListener('mousemove', (e) => {
            let rect = miniCanvas.getBoundingClientRect();
            let targetX = (e.clientX - rect.left) * (miniCanvas.width / rect.width);
            let targetY = (e.clientY - rect.top) * (miniCanvas.height / rect.height);
            miniMouseX += (targetX - miniMouseX) * sensitivity; miniMouseY += (targetY - miniMouseY) * sensitivity;
            miniMouseX = Math.max(0, Math.min(miniCanvas.width, miniMouseX)); miniMouseY = Math.max(0, Math.min(miniCanvas.height, miniMouseY));
        });
        miniCanvas.addEventListener('mousedown', () => {
            let hit = false;
            for(let i = miniTargets.length - 1; i >= 0; i--) {
                if (Math.hypot(miniMouseX - miniTargets[i].x, miniMouseY - miniTargets[i].y) <= miniTargets[i].r) {
                    miniScore += 100; miniCombo++; hit = true; 
                    playRGXSound(); 
                    miniTargets.splice(i, 1); break;
                }
            }
            if(!hit) { miniCombo = 0; miniScore = Math.max(0, miniScore - 20); }
            document.getElementById('mini-score').innerText = "SCORE: " + miniScore;
            document.getElementById('mini-combo').innerText = "COMBO: " + miniCombo;
        });

        rangeCanvas.addEventListener('mousemove', (e) => { 
            let rect = rangeCanvas.getBoundingClientRect(); 
            let targetX = (e.clientX - rect.left) * (rangeCanvas.width / rect.width);
            let targetY = (e.clientY - rect.top) * (rangeCanvas.height / rect.height);
            rMouseX += (targetX - rMouseX) * sensitivity; rMouseY += (targetY - rMouseY) * sensitivity;
            rMouseX = Math.max(0, Math.min(rangeCanvas.width, rMouseX)); rMouseY = Math.max(0, Math.min(rangeCanvas.height, rMouseY));
        });
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
                    playRGXSound(); targets[i] = generateTargetData(); break;
                }
            }
            if (!hitAny) score = Math.max(0, score - 20); updateDashboard();
        }

        function handleRangeClick() {
            for(let i=0; i<rangeUIBox.length; i++) {
                let box = rangeUIBox[i];
                if (rMouseX >= box.x && rMouseX <= box.x + box.w && rMouseY >= box.y && rMouseY <= box.y + box.h) {
                    playRGXSound();
                    if (box.id === 'start' && !isRangePlaying) { isRangePlaying = true; rangeScore = 0; initRangeBots(); }
                    if (box.id === 'clear') { isRangePlaying = false; rangeBots = []; }
                    return;
                }
            }
            if (!isRangePlaying) return;

            let spreadMult = Math.abs(rangePlayerVx) * 11.5; 
            let finalMouseX = rMouseX + (Math.random() - 0.5) * spreadMult;
            let finalMouseY = rMouseY + (Math.random() - 0.5) * spreadMult;

            let hit = false;
            for(let i = rangeBots.length - 1; i >= 0; i--) {
                let b = rangeBots[i];
                if (Math.hypot(finalMouseX - b.x, finalMouseY - b.headY) <= b.headR) {
                    rangeScore++; hit = true; 
                    playRGXSound(); 
                    // 처치된 봇은 겹치지 않는 새로운 좌우 라인 좌표로 개별 재생성
                    rangeBots[i] = createSingleBot(i); break;
                }
            }
            document.getElementById('range-dashboard').innerText = `[THE RANGE] HEADSHOTS: ${rangeScore}`;
        }

        function initTargets() { targets = []; let count = (mode === 'gridshot') ? 3 : 1; for(let i=0; i<count; i++) targets.push(generateTargetData()); }
        function generateTargetData() {
            let spec = diffSpecs[difficulty];
            let baseRadius = 16 * spec.sizeMult; let baseSpeed = 2.5 * spec.speedMult;
            if (mode === 'tracking') return { x: 445, y: 180, radius: 22 * spec.sizeMult, angle: Math.random() * Math.PI * 2, speed: baseSpeed * 1.2 };
            if (mode === 'microflex') return { x: 250 + Math.random() * 380, y: 120 + Math.random() * 120, radius: 10 * spec.sizeMult, life: 75, maxLife: 75 };
            if (mode === 'breaking') return { x: 150 + Math.random() * 580, y: 210, radius: 16 * spec.sizeMult, vx: (Math.random() > 0.5 ? 1 : -1) * baseSpeed, vy: 0 };
            return { x: 120 + Math.random() * 650, y: 80 + Math.random() * 200, radius: baseRadius, vx: 0, vy: 0 };
        }

        // ★ [리얼 사격장 시스템] 봇들이 전방 가로축(X축) 라인에 균등 분할 배치되어 길게 늘어섭니다.
        function initRangeBots() {
            rangeBots = [];
            for (let i = 0; i < 5; i++) { rangeBots.push(createSingleBot(i)); }
        }
        function createSingleBot(index) {
            // 좌우 폭(550)을 기준으로 구역을 나누어 자연스럽게 늘어선 대형 구축
            let sectorWidth = 400 / 5;
            let startX = 70 + (sectorWidth * index) + (Math.random() * (sectorWidth - 25));
            return {
                x: startX,
                y: 110,
                bodyW: 14, bodyH: 32,
                headY: 94, headR: 5.8,
                vx: 0
            };
        }

        function startSession() { isPlaying = true; score = 0; timeLeft = 30.0; totalShots = 0; hitShots = 0; initTargets(); document.getElementById('start-btn').innerText = "⏱ 진행중"; document.getElementById('quit-btn').style.display = "inline-block"; }
        function quitSession() { 
            isPlaying = false; 
            if(score > userBestScore) { userBestScore = score; document.getElementById('user-best').innerText = userBestScore.toLocaleString(); }
            document.getElementById('start-btn').innerText = "▶ 훈련 시작"; document.getElementById('quit-btn').style.display = "none"; updateDashboard(); 
        }
        function updateDashboard() { document.getElementById('ui-score').innerText = "SCORE: " + score; document.getElementById('ui-acc').innerText = "ACC: " + (totalShots>0?Math.round((hitShots/totalShots)*100):100) + "%"; document.getElementById('ui-time').innerText = "TIME: " + timeLeft.toFixed(1) + "s"; }

        // ========================================================
        // 🔄 통합 60FPS 프레임 루프 엔진
        // ========================================================
        function loop() {
            // STAGE 01: 메인 에임랩 루프
            ctx.fillStyle = '#090b15'; ctx.fillRect(0, 0, canvas.width, canvas.height);
            if (keys.a) playerVx = Math.max(-5.0, playerVx - 0.7); else if (keys.d) playerVx = Math.min(5.0, playerVx + 0.7); else { playerVx *= 0.65; }
            playerX = Math.max(40, Math.min(canvas.width - 40, playerX + playerVx));

            if (isPlaying) {
                timeLeft -= 1/60; if (timeLeft <= 0) { timeLeft = 0; quitSession(); }
                if (mode === 'tracking') {
                    let t = targets[0]; t.angle += 0.03 * t.speed; t.x += Math.cos(t.angle) * t.speed; t.y += Math.sin(t.angle) * (t.speed * 0.5);
                    if(t.x < 50 || t.x > canvas.width - 50) t.angle = Math.PI - t.angle; if(t.y < 50 || t.y > canvas.height - 100) t.angle = -t.angle;
                    if (isMouseDown && Math.hypot(mouseX - t.x, mouseY - t.y) <= t.radius) { score += 3; updateDashboard(); if(Math.random()<0.08) playRGXSound(); }
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
            ctx.fillStyle = '#ff4655'; ctx.beginPath(); ctx.arc(mouseX, mouseY, 3.5, 0, Math.PI*2); fill();


            // STAGE 02: 손풀기 미니게임 루프
            miniCtx.fillStyle = '#070913'; miniCtx.fillRect(0, 0, miniCanvas.width, miniCanvas.height);
            if (isMiniHovered) {
                if (miniTargets.length < 3 && Math.random() < 0.03) miniTargets.push({ x: 30 + Math.random()*(miniCanvas.width-60), y: 30 + Math.random()*(miniCanvas.height-60), r: 0, maxR: 14+Math.random()*6, grow: true });
                for(let i=miniTargets.length-1; i>=0; i--) {
                    let mt = miniTargets[i]; if(mt.grow) { mt.r += 0.3; if(mt.r >= mt.maxR) mt.grow = false; } else { mt.r -= 0.15; if(mt.r <= 2) { miniTargets.splice(i, 1); miniCombo = 0; continue; } }
                    miniCtx.fillStyle = 'rgba(168, 85, 247, 0.2)'; miniCtx.beginPath(); miniCtx.arc(mt.x, mt.y, mt.r, 0, Math.PI*2); miniCtx.fill();
                    miniCtx.strokeStyle = '#a855f7'; miniCtx.lineWidth = 1.5; miniCtx.stroke();
                }
                miniCtx.fillStyle = '#00ffcc'; miniCtx.beginPath(); miniCtx.arc(miniMouseX, miniMouseY, 3, 0, Math.PI*2); miniCtx.fill();
            } else { miniCtx.fillStyle = '#4b5563'; miniCtx.font = '11px sans-serif'; miniCtx.textAlign = 'center'; miniCtx.fillText("이곳에 커서를 가져오면 손풀기 타겟이 개방됩니다.", miniCanvas.width/2, miniCanvas.height/2); }


            // STAGE 03: 발로란트 와이드 대형 사격장 루프
            rangeCtx.fillStyle = '#090c14'; rangeCtx.fillRect(0, 0, rangeCanvas.width, rangeCanvas.height);
            rangeCtx.fillStyle = '#1e293b'; rangeCtx.fillRect(50, 142, 450, 2); // 하단 베이스 가이드라인 확장
            
            rangeUIBox.forEach(box => {
                rangeCtx.fillStyle = box.id === 'start' ? (isRangePlaying ? '#1e293b' : '#0f766e') : '#991b1b'; rangeCtx.fillRect(box.x, box.y, box.w, box.h);
                rangeCtx.fillStyle = '#ffffff'; rangeCtx.font = 'bold 10px sans-serif'; rangeCtx.textAlign = 'center'; rangeCtx.fillText(box.label, box.x + box.w/2, box.y + box.h/1.5);
            });

            if (keys.a) rangePlayerVx = Math.max(-4.0, rangePlayerVx - 0.5); else if (keys.d) rangePlayerVx = Math.min(4.0, rangePlayerVx + 0.5); else { rangePlayerVx *= 0.65; }
            rangePlayerX = Math.max(50, Math.min(rangeCanvas.width - 50, rangePlayerX + rangePlayerVx));

            if (isRangePlaying) {
                if (rangeBots.length === 0) initRangeBots();
                rangeBots.forEach(b => {
                    rangeCtx.fillStyle = '#334155'; rangeCtx.fillRect(b.x - b.bodyW/2, b.y, b.bodyW, b.bodyH); // 더 견고한 하체 기둥색
                    
                    let hGrad = rangeCtx.createRadialGradient(b.x, b.headY, 0.8, b.x, b.headY, b.headR);
                    hGrad.addColorStop(0, '#ffffff'); hGrad.addColorStop(0.3, '#00ffcc'); hGrad.addColorStop(1, '#0f766e'); // 🟢 RGX 네온 코어 그라데이션
                    rangeCtx.fillStyle = hGrad; rangeCtx.beginPath(); rangeCtx.arc(b.x, b.headY, b.headR, 0, Math.PI*2); rangeCtx.fill();
                    rangeCtx.strokeStyle = '#00ffcc'; rangeCtx.lineWidth = 1; rangeCtx.stroke();
                });
            }

            rangeCtx.fillStyle = '#38bdf8'; rangeCtx.fillRect(rangePlayerX - 15, rangeCanvas.height - 10, 30, 4);

            let spreadOffset = Math.abs(rangePlayerVx) * 3.0;
            rangeCtx.strokeStyle = Math.abs(rangePlayerVx) <= 0.15 ? '#00ffcc' : '#fbbf24'; rangeCtx.lineWidth = 1.6;
            
            rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX - 4 - spreadOffset, rMouseY); rangeCtx.lineTo(rMouseX - 1 - spreadOffset, rMouseY); rangeCtx.stroke();
            rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX + 1 + spreadOffset, rMouseY); rangeCtx.lineTo(rMouseX + 4 + spreadOffset, rMouseY); rangeCtx.stroke();
            rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX, rMouseY - 4 - spreadOffset); rangeCtx.lineTo(rMouseX, rMouseY - 1 - spreadOffset); rangeCtx.stroke();
            rangeCtx.beginPath(); rangeCtx.moveTo(rMouseX, rMouseY + 1 + spreadOffset); rangeCtx.lineTo(rMouseX, rMouseY + 4 + spreadOffset); rangeCtx.stroke();

            window.requestAnimationFrame(loop);
        }

        initTargets(); loop();
    </script>
    """
    st.components.v1.html(html_src, height=820)

if __name__ == "__main__":
    main()
