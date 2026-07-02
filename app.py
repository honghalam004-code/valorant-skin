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
                    <div style="color:#ff4655; font-size:11px; font-weight:bold; margin-bottom:4px;">⚙️ MOUSE SENSITIVITY</div>
                    <input type="range" id="sens-slider" min="0.1" max="4.0" step="0.05" value="1.0" oninput="updateSensitivity(this.value)" style="width:100%; accent-color:#ff4655;">
                    <div style="text-align:right; font-size:13px; font-weight:bold; color:#ff4655; margin-top:2px;" id="sens-val">1.00</div>
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

                <div style="background:#111625; padding:12px; border-radius:6px; border:1px solid #1f2942; height:150px; overflow:hidden;">
                    <div style="color:#00f2fe; font-size:11px; font-weight:bold; margin-bottom:4px;">💡 모드 가이드</div>
                    <div style="font-size:11px; color:#9ca3af; line-height:1.5;" id="mode-tip">
                        <b>GRIDSHOT:</b> 전방의 과녁 3개를 빠르게 제거하는 플릭 훈련장입니다.
                    </div>
                </div>
            </div>
        </div>

        <div style="display:flex; gap:20px; width:100%;">
            
            <div style="flex: 1; background:#111625; padding:12px; border-radius:8px; border:1px solid #1f2942;">
                <h4 style="margin:0 0 6px 0; color:#a855f7; font-size:13px; font-weight:900;">STAGE 02 : EASY AIM POP (손풀기)</h4>
                <div style="display:flex; gap:10px; font-family:monospace; font-size:12px; font-weight:bold; margin-bottom:8px;">
                    <div style="color:#a855f7;" id="mini-score">SCORE: 0</div>
                    <div style="color:#34d399;" id="mini-combo">COMBO: 0</div>
                    <div style="color:#9ca3af; font-size:11px; font-weight:normal;">*마우스를 올리면 활성화</div>
                </div>
                <canvas id="miniCanvas" width="550" height="200" style="background:#070913; border:2px dashed #a855f7; border-radius:6px; cursor:crosshair; width:100%;"></canvas>
            </div>

            <div style="flex: 1; background:#111625; padding:12px; border-radius:8px; border:1px solid #1f2942;">
                <h4 style="margin:0 0 6px 0; color:#ff4655; font-size:13px; font-weight:900;">STAGE 03 : VALORANT THE RANGE (챔피언스 2021 사운드)</h4>
                <div style="display:flex; gap:12px; font-family:monospace; font-size:12px; font-weight:bold; margin-bottom:8px;">
                    <div style="color:#ff4655;" id="range-dashboard">[THE RANGE] HEADSHOTS: 0</div>
                    <div style="color:#38bdf8; font-size:11px; font-weight:normal;">*이동 중 사격 시 탄퍼짐 발생! 정지 후 헤드샷</div>
                </div>
                <canvas id="rangeCanvas" width="550" height="200" style="background:#090c14; border:2px solid #ff4655; border-radius:6px; cursor:none; width:100%;"></canvas>
            </div>

        </div>

    </div>

    <script>
        const canvas = document.getElementById('aimCanvas'); const ctx = canvas.getContext('2d');
        const miniCanvas = document.getElementById('miniCanvas'); const miniCtx = miniCanvas.getContext('2d');
        const rangeCanvas = document.getElementById('rangeCanvas'); const rangeCtx = rangeCanvas.getContext('2d');

        // --- 🎵 챔피언스 2021 특유의 '퍽-+메탈릭 종소리 잔향' 오디오 합성 엔진 ---
        let audioCtx = null;
        function playChampions2021Sound() {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();

                let now = audioCtx.currentTime;

                // LAYER 1: 묵직하게 머리를 때리는 퍽 타격 타임 노이즈 (Heavy Impact)
                let bSize = audioCtx.sampleRate * 0.05;
                let buffer = audioCtx.createBuffer(1, bSize, audioCtx.sampleRate);
                let data = buffer.getChannelData(0);
                for (let i = 0; i < bSize; i++) {
                    let t = i / audioCtx.sampleRate;
                    data[i] = (Math.random() * 2 - 1) * Math.exp(-85 * t) * 0.6;
                }
                let impactSource = audioCtx.createBufferSource();
                impactSource.buffer = buffer;

                let impactFilter = audioCtx.createBiquadFilter();
                impactFilter.type = 'bandpass';
                impactFilter.frequency.setValueAtTime(280, now); // 둔탁한 타격 주파수
                impactFilter.Q.setValueAtTime(2.0, now);

                let impactGain = audioCtx.createGain();
                impactGain.gain.setValueAtTime(0.8, now);
                impactGain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);

                impactSource.connect(impactFilter);
                impactFilter.connect(impactGain);
                impactGain.connect(audioCtx.destination);

                // LAYER 2: 챔피언스 2021 스킨 특유의 공명하는 황금빛 링잉 사운드 (Metallic Ringing)
                // 전자 비프음이 아니라 실제 메탈릭 울림을 만들기 위해 고정 주파수 사인파 레이어 결합
                let ringOsc = audioCtx.createOscillator();
                let ringOsc2 = audioCtx.createOscillator();
                ringOsc.type = 'sine';
                ringOsc2.type = 'sine';
                
                // 챔스 특유의 맑고 깊은 울림 코드로 주파수 튜닝
                ringOsc.frequency.setValueAtTime(880, now);  
                ringOsc2.frequency.setValueAtTime(1320, now); 

                let ringGain = audioCtx.createGain();
                ringGain.gain.setValueAtTime(0.25, now);
                // 여운이 남도록 타격음보다 길게 0.35초간 부드럽게 감쇄 (챔스 킬사운드의 핵심 리버브 효과)
                ringGain.gain.exponentialRampToValueAtTime(0.001, now + 0.35); 

                let ringFilter = audioCtx.createBiquadFilter();
                ringFilter.type = 'highpass';
                ringFilter.frequency.setValueAtTime(600, now);

                ringOsc.connect(ringFilter);
                ringOsc2.connect(ringFilter);
                ringFilter.connect(ringGain);
                ringGain.connect(audioCtx.destination);

                impactSource.start(now);
                ringOsc.start(now);
                ringOsc2.start(now);
                ringOsc.stop(now + 0.36);
                ringOsc2.stop(now + 0.36);

            } catch(e) { console.log(e); }
        }

        // 전역 물리 설계부
        let mode = 'gridshot'; let difficulty = 1; let isPlaying = false; 
        let score = 0; let timeLeft = 30.0; let totalShots = 0; let hitShots = 0;
        let mouseX = 445, mouseY = 180; let rawMouseX = 445, rawMouseY = 180; let isMouseDown = false;
        let playerX = 445; let playerVx = 0; let keys = { a: false, d: false };
        let showMovingError = false; let errorTimer = 0; let sensitivity = 1.0;
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
        let rangeBots = []; let rMouseX = 275, rMouseY = 100;
        
        // 발로란트 제어 박스 오프셋
        const rangeUIBox = [
            { id: 'start', x: 180, y: 15, w: 90, h: 25, label: "🤖 START" },
            { id: 'clear', x: 280, y: 15, w: 90, h: 25, label: "🧹 CLEAR" }
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
            let rect = miniCanvas.getBoundingClientRect(); 
            let mX = (e.clientX - rect.left) * (miniCanvas.width / rect.width); 
            let mY = (e.clientY - rect.top) * (miniCanvas.height / rect.height);
            let hit = false;
            for(let i = miniTargets.length - 1; i >= 0; i--) {
                if (Math.hypot(mX - miniTargets[i].x, mY - miniTargets[i].y) <= miniTargets[i].r) {
                    miniScore += 100; miniCombo++; hit = true; champions2021KillSound(); miniTargets.splice(i, 1); break;
                }
            }
            if(!hit) { miniCombo = 0; miniScore = Math.max(0, miniScore - 20); }
            document.getElementById('mini-score').innerText = "SCORE: " + miniScore;
            document.getElementById('mini-combo').innerText = "COMBO: " + miniCombo;
        });

        rangeCanvas.addEventListener('mousemove', (e) => { let rect = rangeCanvas.getBoundingClientRect(); rMouseX = (e.clientX - rect.left) * (rangeCanvas.width / rect.width); rMouseY = (e.clientY - rect.top) * (rangeCanvas.height / rect.height); });
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
                    playChampions2021Sound(); targets[i] = generateTargetData(); break;
                }
            }
            if (!hitAny) score = Math.max(0, score - 20); updateDashboard();
        }

        function handleRangeClick() {
            for(let i=0; i<rangeUIBox.length; i++) {
                let box = rangeUIBox[i];
                if (rMouseX >= box.x && rMouseX <= box.x + box.w && rMouseY >= box.y && rMouseY <= box.y + box.h) {
                    playChampions2021Sound();
                    if (box.id === 'start' && !isRangePlaying) { isRangePlaying = true; rangeScore = 0; spawnRangeBot(); }
                    if (box.id === 'clear') { isRangePlaying = false; rangeBots = []; }
                    return;
                }
            }
            if (!isRangePlaying) return;

            // 🛠️ 이동 중 사격 시 발로란트 무빙 스프레드(탄퍼짐) 물리 연산
            let spreadMult = Math.abs(rangePlayerVx) * 11.5; 
            let finalMouseX = rMouseX + (Math.random() - 0.5) * spreadMult;
            let finalMouseY = rMouseY + (Math.random() - 0.5) * spreadMult;

            let hit = false;
            for(let i = rangeBots.length - 1; i >= 0; i--) {
                let b = rangeBots[i];
                // 머리 판정 영역 매칭
                if (Math.hypot(finalMouseX - b.x, finalMouseY - b.headY) <= b.headR) {
                    rangeScore++; hit = true; 
                    playChampions2021Sound(); // 🏆 챔피언스 2021 오디오 피드백
                    rangeBots.splice(i, 1); spawnRangeBot(); break;
                }
            }
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

        function spawnRangeBot() {
            rangeBots = [{
                x: 140 + Math.random() * 270,
                y: 105,
                bodyW: 16, bodyH: 34,
                headY: 88, headR: 6.5,
                vx: (Math.random() > 0.5 ? 1 : -1) * 1.3
            }];
        }

        function updateSensitivity(val) { sensitivity = parseFloat(val); document.getElementById('sens-val').innerText = sensitivity.toFixed(2); }
        function startSession() { isPlaying = true; score = 0; timeLeft = 30.0; totalShots = 0; hitShots = 0; initTargets(); document.getElementById('start-btn').innerText = "⏱ 진행중"; document.getElementById('quit-btn').style.display = "inline-block"; }
        function quitSession() { isPlaying = false; document.getElementById('start-btn').innerText = "▶ 훈련 시작"; document.getElementById('quit-btn').style.display = "none"; updateDashboard(); }
        function updateDashboard() { document.getElementById('ui-score').innerText = "SCORE: " + score; document.getElementById('ui-acc').innerText = "ACC: " + (totalShots>0?Math.round((hitShots/totalShots)*100):100) + "%"; document.getElementById('ui-time').innerText = "TIME: " + timeLeft.toFixed(1) + "s"; }

        // ========================================================
        // 🔄 프레임 제어 통합 엔진
        // ========================================================
        function loop() {
            // STAGE 01: 메인 에임랩 루프
            ctx.fillStyle = '#090b15'; ctx.fillRect(0, 0, canvas.width, canvas.height);
            if (keys.a) playerVx = Math.max(-5.0, playerVx - 0.7); else if (keys.d) playerVx = Math.min(5.0, playerVx + 0.7); else { playerVx *= 0.65; }
            playerX = Math.max(40, Math.min(canvas.width - 40, playerX + playerVx)); mouseX = rawMouseX; mouseY = rawMouseY;

            if (isPlaying) {
                timeLeft -= 1/60; if (timeLeft <= 0) { timeLeft = 0; quitSession(); }
                if (mode === 'tracking') {
                    let t = targets[0]; t.angle += 0.03 * t.speed; t.x += Math.cos(t.angle) * t.speed; t.y += Math.sin(t.angle) * (t.speed * 0.5);
                    if(t.x < 50 || t.x > canvas.width - 50) t.angle = Math.PI - t.angle; if(t.y < 50 || t.y > canvas.height - 100) t.angle = -t.angle;
                    if (isMouseDown && Math.hypot(mouseX - t.x, mouseY - t.y) <= t.radius) { score += 3; updateDashboard(); if(Math.random()<0.08) playChampions2021Sound(); }
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


            // STAGE 02: 손풀기 미니게임 루프
            miniCtx.fillStyle = '#070913'; miniCtx.fillRect(0, 0, miniCanvas.width, miniCanvas.height);
            if (isMiniHovered) {
                if (miniTargets.length < 3 && Math.random() < 0.03) miniTargets.push({ x: 30 + Math.random()*(miniCanvas.width-60), y: 30 + Math.random()*(miniCanvas.height-60), r: 0, maxR: 14+Math.random()*6, grow: true });
                for(let i=miniTargets.length-1; i>=0; i--) {
                    let mt = miniTargets[i]; if(mt.grow) { mt.r += 0.3; if(mt.r >= mt.maxR) mt.grow = false; } else { mt.r -= 0.15; if(mt.r <= 2) { miniTargets.splice(i, 1); miniCombo = 0; continue; } }
                    miniCtx.fillStyle = 'rgba(168, 85, 247, 0.2)'; miniCtx.beginPath(); miniCtx.arc(mt.x, mt.y, mt.r, 0, Math.PI*2); miniCtx.fill();
                    miniCtx.strokeStyle = '#a855f7'; miniCtx.lineWidth = 1.5; miniCtx.stroke();
                }
            } else { miniCtx.fillStyle = '#4b5563'; miniCtx.font = '11px sans-serif'; miniCtx.textAlign = 'center'; miniCtx.fillText("이곳에 커서를 가져오면 손풀기 타겟이 개방됩니다.", miniCanvas.width/2, miniCanvas.height/2); }


            // STAGE 03: ★ 발로란트 무제한 연습장 루프 (연습장 완전 동기화)
            rangeCtx.fillStyle = '#090c14'; rangeCtx.fillRect(0, 0, rangeCanvas.width, rangeCanvas.height);
            
            // 철제 스폰 발판 가로 구조선
            rangeCtx.fillStyle = '#1e293b'; rangeCtx.fillRect(80, 140, 390, 3); 
            
            // START / CLEAR 디스플레이 대시 패널 스위치
            rangeUIBox.forEach(box => {
                rangeCtx.fillStyle = box.id === 'start' ? (isRangePlaying ? '#1e293b' : '#0f766e') : '#991b1b'; rangeCtx.fillRect(box.x, box.y, box.w, box.h);
                rangeCtx.fillStyle = '#ffffff'; rangeCtx.font = 'bold 10px sans-serif'; rangeCtx.textAlign = 'center'; rangeCtx.fillText(box.label, box.x + box.w/2, box.y + box.h/1.5);
            });

            if (keys.a) rangePlayerVx = Math.max(-4.0, rangePlayerVx - 0.5); else if (keys.d) rangePlayerVx = Math.min(4.0, rangePlayerVx + 0.5); else { rangePlayerVx *= 0.65; }
            rangePlayerX = Math.max(50, Math.min(rangeCanvas.width - 50, rangePlayerX + rangePlayerVx));

            if (isRangePlaying) {
                if (rangeBots.length === 0) spawnRangeBot();
                rangeBots.forEach(b => {
                    b.x += b.vx; if(b.x < 110 || b.x > 440) b.vx *= -1;
                    
                    // 철제 트레이닝 봇 몸통 구현 (발로란트 샌드백 로봇 테마 컬러 적용)
                    rangeCtx.fillStyle = '#475569'; rangeCtx.fillRect(b.x - b.bodyW/2, b.y, b.bodyW, b.bodyH);
                    
                    // 헤드샷 전용 과녁 머리 (식별이 뚜렷한 입체 그라데이션)
                    let hGrad = rangeCtx.createRadialGradient(b.x, b.headY, 1, b.x, b.headY, b.headR);
                    hGrad.addColorStop(0, '#ffffff'); hGrad.addColorStop(1, '#ff4655');
                    rangeCtx.fillStyle = hGrad; rangeCtx.beginPath(); rangeCtx.arc(b.x, b.headY, b.headR, 0, Math.PI*2); rangeCtx.fill();
                    rangeCtx.strokeStyle = '#ffffff'; rangeCtx.lineWidth = 1; rangeCtx.stroke();
                });
            }

            // 하단 조작 디바이스 지시패드
            rangeCtx.fillStyle = '#38bdf8'; rangeCtx.fillRect(rangePlayerX - 15, rangeCanvas.height - 10, 30, 4);

            // 🎯 무빙 속도 연동 가변 크로스헤어 (탄퍼짐 가시화)
            let spreadOffset = Math.abs(rangePlayerVx) * 3.0;
            // 정지 상태일 땐 완벽한 녹색 조준선, 이동 중엔 경고 오차 황색 조준선 가동
            rangeCtx.strokeStyle = Math.abs(rangePlayerVx) <= 0.15 ? '#22c55e' : '#fbbf24'; rangeCtx.lineWidth = 1.6;
            
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
