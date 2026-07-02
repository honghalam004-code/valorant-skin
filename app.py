import streamlit as st

def main():
    st.set_page_config(page_title="AIMLAB: PREMIUM AUDIO & MINI GAME", layout="wide")

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

    st.markdown("<h2 style='text-align:center; color:#ff4655; font-weight:900;'>🎯 AIMLAB: ADVANCED V3</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#4b5563; font-size:14px;'>타격감 킬사운드 리뉴얼 완료 | 하단 '클래식 에임 팝' 서브 미니 게임 오픈</p>", unsafe_allow_html=True)

    html_src = """
    <div style="max-width:1240px; margin:0 auto; display:flex; flex-direction:column; gap:25px;">
        
        <div style="display:flex; gap:20px; justify-content:center;">
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
                    <canvas id="aimCanvas" width="860" height="460" style="background:#090b11; border:2px solid #1f2937; border-radius:6px; cursor:none;"></canvas>
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
                    <div id="record-board" style="font-family:monospace; font-size:13px; display:flex; flex-direction:column; gap:8px; color:#e5e7eb;"></div>
                    <button onclick="clearAllData()" style="margin-top:auto; background:transparent; color:#4b5563; border:1px solid #374151; padding:6px; font-size:11px; cursor:pointer; border-radius:4px; font-weight:bold;">기록 초기화</button>
                </div>
            </div>
        </div>

        <div style="background:#111827; padding:20px; border-radius:8px; border:1px solid #1f2937; display:flex; gap:20px; align-items:center;">
            <div style="flex:1; text-align:left;">
                <h3 style="margin:0 0 5px 0; color:#38bdf8; font-weight:800;">🎮 MINI GAME : CLASSIC AIM POP</h3>
                <p style="margin:0 0 15px 0; color:#9ca3af; font-size:13px;">무작위로 커졌다 사라지는 풍선 표적을 신속하게 터트리세요! 손풀기 및 순발력 최적화용 서브 게임입니다.</p>
                
                <div style="display:flex; gap:20px; font-family:monospace; font-size:15px; font-weight:bold; background:#07080b; padding:12px; border-radius:6px; border:1px solid #1f2937; margin-bottom:12px;">
                    <div style="color:#38bdf8;" id="mini-score">POP SCORE: 0</div>
                    <div style="color:#ef4444;" id="mini-life">LIFE: ❤️❤️❤️</div>
                    <div style="color:#eab308;" id="mini-time">TIME: 20.0s</div>
                    <div style="color:#a855f7; margin-left:auto;" id="mini-best">BEST: 0</div>
                </div>
                <button onclick="startMiniGame()" id="mini-start-btn" style="background:linear-gradient(135deg, #38bdf8, #0284c7) !important; color:white; font-weight:bold; padding:12px; border-radius:4px; width:100%; cursor:pointer; border:none;">🎯 미니게임 시작 (20초 팝업 챌린지)</button>
            </div>
            <div>
                <canvas id="miniCanvas" width="500" height="210" style="background:#07080b; border:1px solid #374151; border-radius:6px; cursor:crosshair;"></canvas>
            </div>
        </div>
    </div>

    <script>
        // --- 캔버스 기초 선언 ---
        const canvas = document.getElementById('aimCanvas');
        const ctx = canvas.getContext('2d');
        const miniCanvas = document.getElementById('miniCanvas');
        const miniCtx = miniCanvas.getContext('2d');

        // --- 🎵 오디오 엔진 리뉴얼 (찰지고 묵직한 오인격 FPS 타격음) ---
        let audioCtx = null;
        function playKillSound() {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                
                let now = audioCtx.currentTime;
                
                // 1. 묵직하게 때려박는 타격 베이스 라인 (사인을 이용한 초단기 드롭 부밍)
                let bodyOsc = audioCtx.createOscillator();
                let bodyGain = audioCtx.createGain();
                bodyOsc.type = 'sine';
                bodyOsc.frequency.setValueAtTime(320, now);
                bodyOsc.frequency.exponentialRampToValueAtTime(80, now + 0.08);
                bodyGain.gain.setValueAtTime(0.3, now);
                bodyGain.gain.exponentialRampToValueAtTime(0.01, now + 0.08);
                bodyOsc.connect(bodyGain);
                bodyGain.connect(audioCtx.destination);
                bodyOsc.start(now);
                bodyOsc.stop(now + 0.08);

                // 2. 금속성 재질의 헤드샷 크랙 클리커 (하이패싱 메탈 스냅 스파크)
                let snapOsc = audioCtx.createOscillator();
                let snapGain = audioCtx.createGain();
                snapOsc.type = 'triangle';
                snapOsc.frequency.setValueAtTime(950, now);
                snapOsc.frequency.setValueAtTime(1400, now + 0.02);
                snapGain.gain.setValueAtTime(0.15, now);
                snapGain.gain.exponentialRampToValueAtTime(0.005, now + 0.05);
                snapOsc.connect(snapGain);
                snapGain.connect(audioCtx.destination);
                snapOsc.start(now);
                snapOsc.stop(now + 0.05);
            } catch(e) {}
        }

        // --- 메인 게임용 전역 변수 컴포넌트 ---
        let mode = 'breaking'; let difficulty = 1; let sensitivity = 1.0;
        let isPlaying = false; let score = 0; let timeLeft = 30.0; let totalShots = 0; let hitShots = 0;
        let playerLives = 2; let mouseX = 430, mouseY = 230; let rawMouseX = 430, rawMouseY = 230;
        let isMouseDown = false;

        let playerX = 430; let playerVx = 0;
        const playerMaxSpeed = 6.0; const playerAcc = 0.9; const playerFric = 0.55;
        let keys = { a: false, d: false };
        let showMovingError = false; let errorTimer = 0;

        let projectiles = []; let enemyShootTimer = 0; let showHitEffect = false; let hitEffectTimer = 0;
        let highScores = { gridshot: 0, tracking: 0, microflex: 0, breaking: 0 };
        let targets = [];

        const diffSpecs = {
            1: { radiusBonus: 1.4, speedBonus: 0.6, projectileSpeed: 2.5, desc: "<strong>🟢 레벨 1 사양:</strong><br>과녁 반경: 1.4배 상향<br>투사체 속도: 느림" },
            2: { radiusBonus: 1.1, speedBonus: 1.1, projectileSpeed: 4.0, desc: "<strong>🟡 레벨 2 사양:</strong><br>과녁 반경: 실전 입문 규격<br>투사체 속도: 보통" },
            3: { radiusBonus: 0.9, speedBonus: 1.6, projectileSpeed: 5.5, desc: "<strong>🟠 레벨 3 사양:</strong><br>과녁 반경: 10% 축소 정밀전<br>투사체 속도: 빠름" },
            4: { radiusBonus: 0.75, speedBonus: 2.2, projectileSpeed: 7.0, desc: "<strong>🔴 레벨 4 사양 (밸런스 패치):</strong><br>과녁 반경: 현실적인 마이크로 타겟팅 (0.75배)<br>투사체 속도: 극속 대응 훈련" }
        };

        // --- 🎮 보너스 미니 게임 전역 변수 컴포넌트 ---
        let isMiniPlaying = false; let miniScore = 0; let miniTimeLeft = 20.0; let miniLives = 3; let miniBestScore = 0;
        let miniTargets = [];

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
            rawMouseX = e.clientX - rect.left; rawMouseY = e.clientY - rect.top;
        });
        canvas.addEventListener('mousedown', () => { isMouseDown = true; });
        window.addEventListener('mouseup', () => { isMouseDown = false; });

        // --- 미니게임 전용 마우스 클릭 바인딩 ---
        miniCanvas.addEventListener('mousedown', (e) => {
            if (!isMiniPlaying) return;
            let rect = miniCanvas.getBoundingClientRect();
            let mX = e.clientX - rect.left;
            let mY = e.clientY - rect.top;

            let hit = false;
            for(let i = miniTargets.length - 1; i >= 0; i--) {
                let t = miniTargets[i];
                let dist = Math.hypot(mX - t.x, mY - t.y);
                if (dist <= t.currentRadius) {
                    miniScore += 150;
                    playKillSound(); // 무조건 리뉴얼된 타격 킬사운드 공유 공유!
                    miniTargets.splice(i, 1);
                    hit = true; break;
                }
            }
            if (!hit) miniScore = Math.max(0, miniScore - 40);
            updateMiniUI();
        });

        function loadSavedScores() {
            if (localStorage.getItem('aimlab_v9_hs')) highScores = JSON.parse(localStorage.getItem('aimlab_v9_hs'));
            if (localStorage.getItem('aimlab_v9_minibest')) miniBestScore = parseInt(localStorage.getItem('aimlab_v9_minibest')) || 0;
            if (localStorage.getItem('aimlab_v9_sens')) {
                sensitivity = parseFloat(localStorage.getItem('aimlab_v9_sens'));
                document.getElementById('sens-slider').value = sensitivity;
                document.getElementById('sens-val').innerText = sensitivity.toFixed(2);
            }
            renderScoresUI(); updateMiniUI();
        }

        function saveScores() { 
            localStorage.setItem('aimlab_v9_hs', JSON.stringify(highScores));
            localStorage.setItem('aimlab_v9_minibest', miniBestScore);
        }

        function updateSensitivity(val) {
            sensitivity = parseFloat(val);
            document.getElementById('sens-val').innerText = sensitivity.toFixed(2);
            localStorage.setItem('aimlab_v9_sens', sensitivity);
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

        function clearAllData() { highScores = { gridshot: 0, tracking: 0, microflex: 0, breaking: 0 }; miniBestScore = 0; saveScores(); renderScoresUI(); updateMiniUI(); }

        function setDifficulty(lvl) {
            if (isPlaying) return;
            difficulty = lvl;
            const colorMap = { 1: '#22c55e', 2: '#eab308', 3: '#f97316', 4: '#ef4444' };
            for(let i=1; i<=4; i++) {
                const btn = document.getElementById('df-' + i);
                if (i === lvl) { btn.style.background = colorMap[lvl]; btn.style.color = 'black'; btn.style.border = 'none'; } 
                else { btn.style.background = '#07080b'; btn.style.color = '#e5e7eb'; btn.style.border = '1px solid #374151'; }
            }
            document.getElementById('df-desc').innerHTML = diffSpecs[lvl].desc;
            initTargets();
        }

        function changeMode(m) {
            mode = m;
            ['grid', 'track', 'micro', 'break'].forEach(k => {
                const el = document.getElementById('m-' + k);
                let targetKey = m.substring(0,5); if (m === 'breaking') targetKey = 'break';
                if (k === targetKey) { el.style.background = m === 'breaking' ? '#ff4655' : '#00f2fe'; el.style.color = 'black'; el.style.border = 'none'; } 
                else { el.style.background = '#07080b'; el.style.color = k === 'break' ? '#ff4655' : '#00f2fe'; el.style.border = '1px solid currentColor'; }
            });
            if (isPlaying) quitSession();
            initTargets(); updateDashboard();
        }

        function initTargets() {
            targets = []; projectiles = [];
            let count = (mode === 'gridshot') ? 3 : 1;
            for(let i=0; i<count; i++) targets.push(generateTargetData());
        }

        function generateTargetData() {
            let baseRadius = 18; let baseSpeed = 3.5;
            if (mode === 'tracking') { baseRadius = 22; baseSpeed = 4.5; }
            else if (mode === 'microflex') { baseRadius = 16; baseSpeed = 4.0; } 
            else if (mode === 'breaking') { baseRadius = 18; baseSpeed = 2.0; }
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
            if (isMiniPlaying) stopMiniGame(); // 미니게임 중이면 인터럽트 차단 리셋
            isPlaying = true; canvas.style.cursor = "none";
            score = 0; timeLeft = 30.0; totalShots = 0; hitShots = 0; playerLives = 2;
            playerX = 430; playerVx = 0; enemyShootTimer = 0; projectiles = [];
            initTargets();
            document.getElementById('start-btn').style.background = '#4b5563';
            document.getElementById('start-btn').innerText = "⏱ 훈련 진행중";
            document.getElementById('quit-btn').style.display = "inline-block";
        }

        function quitSession() {
            isPlaying = false; canvas.style.cursor = "default";
            document.getElementById('start-btn').style.background = '#34d399';
            document.getElementById('start-btn').innerText = "▶ 훈련 시작";
            document.getElementById('quit-btn').style.display = "none";
            projectiles = []; updateDashboard();
        }

        function endSession() {
            isPlaying = false; canvas.style.cursor = "default";
            document.getElementById('start-btn').style.background = '#34d399';
            document.getElementById('start-btn').innerText = "▶ 훈련 시작";
            document.getElementById('quit-btn').style.display = "none";
            if (score > (highScores[mode] || 0)) { highScores[mode] = score; saveScores(); renderScoresUI(); }
        }

        canvas.addEventListener('mousedown', () => {
            if (!isPlaying) return; if (mode === 'tracking') return;
            totalShots++; let hitAny = false;
            for (let i = 0; i < targets.length; i++) {
                let dist = Math.hypot(mouseX - targets[i].x, mouseY - targets[i].y);
                if (dist <= targets[i].radius) {
                    if (mode === 'breaking' && Math.abs(playerVx) > 0.2) {
                        score = Math.max(0, score - 40); showMovingError = true; errorTimer = 25; updateDashboard(); return;
                    }
                    hitShots++; score += 100; hitAny = true;
                    playKillSound(); // 교체된 명품 사운드 출력
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

        // --- 🎮 보너스 미니게임 코어 로직 제어 함수 ---
        function startMiniGame() {
            if (isMiniPlaying) return;
            if (isPlaying) quitSession(); // 메인 게임 작동 중이면 중단 유도
            isMiniPlaying = true;
            miniScore = 0; miniTimeLeft = 20.0; miniLives = 3; miniTargets = [];
            document.getElementById('mini-start-btn').innerText = "💥 POPPING RUNNING...";
            document.getElementById('mini-start-btn').style.background = "#4b5563";
            updateMiniUI();
        }

        function stopMiniGame() {
            isMiniPlaying = false;
            document.getElementById('mini-start-btn').innerText = "🎯 미니게임 시작 (20초 팝업 챌린지)";
            document.getElementById('mini-start-btn').style.background = "linear-gradient(135deg, #38bdf8, #0284c7)";
            if (miniScore > miniBestScore) { miniBestScore = miniScore; saveScores(); }
            updateMiniUI();
        }

        function updateMiniUI() {
            document.getElementById('mini-score').innerText = "POP SCORE: " + miniScore;
            document.getElementById('mini-time').innerText = "TIME: " + Math.max(0, miniTimeLeft).toFixed(1) + "s";
            let hearts = ""; for(let i=0; i<3; i++) hearts += (i < miniLives) ? "❤️" : "💔";
            document.getElementById('mini-life').innerText = "LIFE: " + hearts;
            document.getElementById('mini-best').innerText = "BEST: " + miniBestScore;
        }

        function spawnMiniTarget() {
            if (miniTargets.length < 3 && Math.random() < 0.04) {
                miniTargets.push({
                    x: 40 + Math.random() * (miniCanvas.width - 80),
                    y: 40 + Math.random() * (miniCanvas.height - 80),
                    maxRadius: 18 + Math.random() * 12,
                    currentRadius: 0,
                    state: 'growing', // 'growing' -> 'shrinking'
                    speed: 0.4 + Math.random() * 0.5
                });
            }
        }

        // --- 통합 메인 애니메이션 무한 루프 시스템 ---
        function loop() {
            // 1. 메인 엔진 드로잉 스케줄러
            if (showHitEffect && hitEffectTimer > 0) {
                ctx.fillStyle = '#260a0f'; hitEffectTimer--;
                if(hitEffectTimer <= 0) showHitEffect = false;
            } else { ctx.fillStyle = '#090b11'; }
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.strokeStyle = '#121620'; ctx.lineWidth = 1;
            for(let i=0; i<canvas.width; i+=50) { ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,canvas.height); ctx.stroke(); }
            for(let j=0; j<canvas.height; j+=50) { ctx.beginPath(); ctx.moveTo(0,j); ctx.lineTo(canvas.width,j); ctx.stroke(); }

            if (keys.a) playerVx = Math.max(-playerMaxSpeed, playerVx - playerAcc);
            else if (keys.d) playerVx = Math.min(playerMaxSpeed, playerVx + playerAcc);
            else {
                if (playerVx > 0) playerVx = Math.max(0, playerVx - playerFric);
                else if (playerVx < 0) playerVx = Math.min(0, playerVx + playerFric);
            }
            playerX = Math.max(40, Math.min(canvas.width - 40, playerX + playerVx));

            let spreadX = 0, spreadY = 0;
            if (mode === 'breaking' && Math.abs(playerVx) > 0.2) {
                spreadX = (Math.random() - 0.5) * (Math.abs(playerVx) * 12);
                spreadY = (Math.random() - 0.5) * (Math.abs(playerVx) * 12);
            }
            mouseX = rawMouseX + spreadX; mouseY = rawMouseY + spreadY;

            if (isPlaying) {
                timeLeft -= 1/60; if (timeLeft <= 0) { timeLeft = 0; endSession(); }
                updateDashboard();

                if (mode === 'tracking' && isMouseDown) {
                    targets.forEach((t) => {
                        let dist = Math.hypot(mouseX - t.x, mouseY - t.y);
                        if (dist <= t.radius) score += 2;
                    });
                }

                if (mode === 'breaking') {
                    enemyShootTimer++;
                    let shootInterval = difficulty === 1 ? 70 : (difficulty === 2 ? 50 : (difficulty === 3 ? 35 : 24));
                    if (enemyShootTimer >= shootInterval && targets.length > 0) {
                        enemyShootTimer = 0; let t = targets[0];
                        let dx = playerX - t.x; let dy = (canvas.height - 20) - t.y; let dist = Math.hypot(dx, dy);
                        let speed = diffSpecs[difficulty].projectileSpeed;
                        projectiles.push({ x: t.x, y: t.y, vx: (dx / dist) * speed, vy: (dy / dist) * speed, radius: 6 });
                    }
                }

                for (let i = projectiles.length - 1; i >= 0; i--) {
                    let p = projectiles[i]; p.x += p.vx; p.y += p.vy;
                    if (p.y >= canvas.height - 25 && p.y <= canvas.height - 10) {
                        if (p.x >= playerX - 30 && p.x <= playerX + 30) {
                            playerLives--; showHitEffect = true; hitEffectTimer = 10; projectiles.splice(i, 1);
                            if (playerLives <= 0) { quitSession(); alert("💥 게임 오버! 발사체에 한계 피격되었습니다."); break; }
                            continue;
                        }
                    }
                    if (p.y > canvas.height || p.x < 0 || p.x > canvas.width) { projectiles.splice(i, 1); continue; }
                    ctx.save(); ctx.fillStyle = '#f59e0b'; ctx.shadowColor = '#ef4444'; ctx.shadowBlur = 8;
                    ctx.beginPath(); ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2); ctx.fill(); ctx.restore();
                }

                targets.forEach((t) => {
                    t.x += t.vx; t.y += t.vy;
                    if(t.x - t.radius < 15 || t.x + t.radius > canvas.width - 15) t.vx *= -1;
                    if(t.y - t.radius < 15 || t.y + t.radius > canvas.height - 15) t.vy *= -1;
                    ctx.save();
                    if(mode === 'gridshot') ctx.strokeStyle = '#38bdf8';
                    else if(mode === 'tracking') { ctx.strokeStyle = '#00f2fe'; ctx.fillStyle = 'rgba(0, 242, 254, 0.1)'; ctx.fill(); } 
                    else if(mode === 'microflex') ctx.strokeStyle = '#f43f5e';
                    else { ctx.strokeStyle = '#ff4655'; ctx.shadowColor = '#ff4655'; ctx.shadowBlur = 6; }
                    ctx.lineWidth = 2.5; ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI*2); ctx.stroke(); ctx.restore();
                });
            } else {
                ctx.fillStyle = 'rgba(255,255,255,0.2)'; ctx.font = '14px sans-serif'; ctx.textAlign = 'center';
                ctx.fillText("메인 에임 세션 준비 완료 | 아래에는 미니게임 팝 엔진이 준비되어 있습니다.", canvas.width/2, canvas.height/2);
            }

            if (showMovingError && errorTimer > 0) {
                ctx.save(); ctx.fillStyle = '#ff4655'; ctx.font = 'bold 20px sans-serif'; ctx.textAlign = 'center';
                ctx.fillText("❌ 무빙샷 불허 (탄퍼짐 발생!)", canvas.width/2, 70); ctx.restore();
                errorTimer--; if(errorTimer <= 0) showMovingError = false;
            }

            ctx.save(); ctx.fillStyle = Math.abs(playerVx) <= 0.2 ? '#22c55e' : '#eab308';
            ctx.fillRect(playerX - 25, canvas.height - 25, 50, 10); ctx.fillStyle = '#e5e7eb'; ctx.font = '11px sans-serif'; ctx.textAlign = 'center';
            if (mode === 'breaking' && isPlaying) { ctx.fillText("HP: " + (playerLives === 2 ? "❤️❤️" : "❤️💔"), playerX, canvas.height - 35); } 
            else { ctx.fillText("PLAYER", playerX, canvas.height - 35); } ctx.restore();

            ctx.save(); ctx.fillStyle = '#FF0000'; ctx.beginPath(); ctx.arc(mouseX, mouseY, 3.5, 0, Math.PI * 2); ctx.fill(); ctx.restore();


            // 2. 🎮 보너스 미니 게임 드로잉 및 주기 연산 스케줄러
            miniCtx.fillStyle = '#07080b'; miniCtx.fillRect(0, 0, miniCanvas.width, miniCanvas.height);
            miniCtx.strokeStyle = '#141b2e'; miniCtx.lineWidth = 1;
            for(let x=0; x<miniCanvas.width; x+=40) { miniCtx.beginPath(); miniCtx.moveTo(x,0); miniCtx.lineTo(x,miniCanvas.height); miniCtx.stroke(); }
            for(let y=0; y<miniCanvas.height; y+=40) { miniCtx.beginPath(); miniCtx.moveTo(0,y); miniCtx.lineTo(miniCanvas.width,y); miniCtx.stroke(); }

            if (isMiniPlaying) {
                miniTimeLeft -= 1/60; spawnMiniTarget(); updateMiniUI();
                if (miniTimeLeft <= 0) { miniTimeLeft = 0; stopMiniGame(); alert("⏱ 타임 오버! 미니게임 챌린지가 끝났습니다."); }

                for(let i = miniTargets.length - 1; i >= 0; i--) {
                    let mt = miniTargets[i];
                    if (mt.state === 'growing') {
                        mt.currentRadius += mt.speed;
                        if (mt.currentRadius >= mt.maxRadius) mt.state = 'shrinking';
                    } else {
                        mt.currentRadius -= mt.speed * 0.7;
                        if (mt.currentRadius <= 1) {
                            // 플레이어가 터트리지 못하고 완전히 소멸했을 때 라이프 아웃 패널티 처리
                            miniTargets.splice(i, 1); miniLives--; updateMiniUI();
                            if (miniLives <= 0) { stopMiniGame(); alert("💥 라이프 아웃! 하트가 전부 소멸되어 종료되었습니다."); break; }
                            continue;
                        }
                    }

                    // 예쁜 네온 그라데이션 풍선 렌더링
                    miniCtx.save();
                    miniCtx.beginPath(); miniCtx.arc(mt.x, mt.y, mt.currentRadius, 0, Math.PI * 2);
                    miniCtx.fillStyle = 'rgba(56, 189, 248, 0.2)'; miniCtx.fill();
                    miniCtx.strokeStyle = '#38bdf8'; miniCtx.lineWidth = 2; miniCtx.stroke();
                    // 타겟 코어 정밀점
                    miniCtx.beginPath(); miniCtx.arc(mt.x, mt.y, 2.5, 0, Math.PI * 2); miniCtx.fillStyle = '#a855f7'; miniCtx.fill();
                    miniCtx.restore();
                }
            } else {
                miniCtx.fillStyle = 'rgba(255,255,255,0.15)'; miniCtx.font = '12px sans-serif'; miniCtx.textAlign = 'center';
                miniCtx.fillText("미니게임 시작 버튼을 누르면 이 화면에 타겟이 활성화됩니다.", miniCanvas.width/2, miniCanvas.height/2);
            }

            requestAnimationFrame(loop);
        }

        loadSavedScores(); initTargets(); loop();
    </script>
    """
    st.components.v1.html(html_src, height=810)

if __name__ == "__main__":
    main()
