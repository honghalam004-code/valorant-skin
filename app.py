import streamlit as st

def main():
    st.set_page_config(page_title="VALORANT: THE RANGE SYSTEM", layout="wide")

    st.markdown("""
        <style>
        .main { background-color: #060914; color: #e5e7eb; font-family: 'Segoe UI', monospace; }
        iframe { border: none !important; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center; color:#ff4655; font-weight:900; letter-spacing:2px;'>🎯 VALORANT: THE RANGE (발로란트 연습장)</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#6b7280; font-size:13px;'>모든 메뉴와 시작은 인게임 과녁을 사격하세요. | 콤보 연속 킬사운드 시스템 탑재</p>", unsafe_allow_html=True)

    html_src = """
    <div style="max-width:1200px; margin:0 auto; display:flex; gap:20px; justify-content:center;">
        
        <div style="flex: 1; text-align:center;">
            <div style="position:relative;">
                <canvas id="rangeCanvas" width="900" height="520" style="background:#0b0e14; border:2px solid #ff4655; border-radius:6px; cursor:none; box-shadow: 0 0 20px rgba(255, 70, 85, 0.15);"></canvas>
            </div>
        </div>

        <div style="width:260px; display:flex; flex-direction:column; gap:15px; text-align:left;">
            <div style="background:#111524; padding:16px; border-radius:6px; border:1px solid #1f2942;">
                <div style="color:#ff4655; font-size:11px; font-weight:bold; letter-spacing:1px; margin-bottom:8px;">⚙️ MOUSE SENSITIVITY</div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <span style="font-size:12px; color:#9ca3af;">조준선 감도</span>
                    <span style="font-size:15px; font-weight:bold; color:#ff4655; font-family:monospace;" id="sens-val">1.00</span>
                </div>
                <input type="range" id="sens-slider" min="0.1" max="4.0" step="0.05" value="1.0" oninput="updateSensitivity(this.value)" style="width:100%; accent-color:#ff4655; cursor:pointer;">
                <div style="font-size:11px; color:#4b5563; margin-top:8px; line-height:1.4;">[A], [D] 키로 하단 발 브레이킹 발판 무빙이 가능합니다.</div>
            </div>

            <div style="background:#111524; padding:16px; border-radius:6px; border:1px solid #1f2942; flex:1; display:flex; flex-direction:column;">
                <div style="color:#00f2fe; font-size:11px; font-weight:bold; letter-spacing:1px; margin-bottom:12px;">🏆 VALORANT LEADERBOARD</div>
                <div id="record-board" style="font-family:monospace; font-size:13px; display:flex; flex-direction:column; gap:10px; color:#e5e7eb;">
                    </div>
                <button onclick="clearAllData()" style="margin-top:auto; background:transparent; color:#4b5563; border:1px solid #223154; padding:6px; font-size:11px; cursor:pointer; border-radius:4px; font-weight:bold;">기록 데이터 초기화</button>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('rangeCanvas');
        const ctx = canvas.getContext('2d');

        // --- 🎵 오디오 엔진 (발로란트 연속 킬 주파수 변조 사운드) ---
        let audioCtx = null;
        function playValorantKillSound(combo) {
            try {
                if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                if (audioCtx.state === 'suspended') audioCtx.resume();
                
                let now = audioCtx.currentTime;
                
                // 연속 콤보 킬수에 따라 음정 피치 상승 (1콤보 ~ 5콤보 이상)
                let baseFreq = 523.25; // C5 기준 음역
                let pitchShift = Math.min(combo, 6) * 110; 
                let targetFreq = baseFreq + pitchShift;

                // 타격 스냅 사운드
                let osc = audioCtx.createOscillator();
                let gain = audioCtx.createGain();
                
                osc.type = 'sine';
                osc.frequency.setValueAtTime(targetFreq, now);
                osc.frequency.exponentialRampToValueAtTime(targetFreq * 1.5, now + 0.03);
                
                gain.gain.setValueAtTime(0.2, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.14);
                
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start(now);
                osc.stop(now + 0.14);

                // 바디 타격 서브 댐핑음
                let subOsc = audioCtx.createOscillator();
                let subGain = audioCtx.createGain();
                subOsc.type = 'triangle';
                subOsc.frequency.setValueAtTime(180, now);
                subGain.gain.setValueAtTime(0.25, now);
                subGain.gain.exponentialRampToValueAtTime(0.01, now + 0.06);
                subOsc.connect(subGain);
                subGain.connect(audioCtx.destination);
                subOsc.start(now);
                subOsc.stop(now + 0.06);
            } catch(e) {}
        }

        // --- 시스템 핵심 변수 제어 ---
        let mode = 'gridshot'; 
        let isPlaying = false; 
        let score = 0; 
        let timeLeft = 30.0;
        let comboCount = 0; 
        let comboTimer = 0;
        let sensitivity = 1.0;
        
        let mouseX = 450, mouseY = 260;
        let rawMouseX = 450, rawMouseY = 260;
        
        let playerX = 450; 
        let playerVx = 0;
        let keys = { a: false, d: false };
        let showMovingError = false; let errorTimer = 0;

        let projectiles = []; let enemyShootTimer = 0;
        let highScores = { gridshot: 0, tracking: 0, microflex: 0, breaking: 0 };
        let targets = [];

        // UI용 사격판(버튼 대용 과녁 오브젝트) 정의
        const uiTargets = [
            { id: 'gridshot', x: 200, y: 55, w: 90, h: 30, label: "🎯 GRID" },
            { id: 'tracking', x: 310, y: 55, w: 90, h: 30, label: "🔄 TRACK" },
            { id: 'microflex', x: 420, y: 55, w: 90, h: 30, label: "⚡ MICRO" },
            { id: 'breaking', x: 530, y: 55, w: 90, h: 30, label: "💥 BREAK" },
            { id: 'start_trigger', x: 320, y: 120, w: 260, h: 40, label: "[ 🤖 START BOT CHALLENGE ]", isAction: true },
            { id: 'quit_trigger', x: 670, y: 55, w: 110, h: 30, label: "🤖 RESPAWN", isAction: true }
        ];

        window.addEventListener('keydown', (e) => {
            if (e.key.toLowerCase() === 'a') keys.a = true;
            if (e.key.toLowerCase() === 'd') keys.d = true;
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

        let isMouseDown = false;
        canvas.addEventListener('mousedown', () => { isMouseDown = true; handleShooting(); });
        window.addEventListener('mouseup', () => { isMouseDown = false; });

        function handleShooting() {
            // 1. 상단 메뉴 및 트리거 사격판 충돌 연산
            for (let i = 0; i < uiTargets.length; i++) {
                let ut = uiTargets[i];
                if (mouseX >= ut.x && mouseX <= ut.x + ut.w && mouseY >= ut.y && mouseY <= ut.y + ut.h) {
                    playValorantKillSound(1); // 메뉴 클릭 타격음 방출

                    if (ut.isAction) {
                        if (ut.id === 'start_trigger' && !isPlaying) startRangeSession();
                        if (ut.id === 'quit_trigger' && isPlaying) quitRangeSession();
                    } else {
                        if (!isPlaying) {
                            mode = ut.id;
                            initBots();
                        }
                    }
                    return;
                }
            }

            if (!isPlaying || mode === 'tracking') return;

            // 2. 인게임 사격 타겟 봇 충돌 연산
            let hitAny = false;
            for (let i = 0; i < targets.length; i++) {
                let dist = Math.hypot(mouseX - targets[i].x, mouseY - targets[i].y);
                if (dist <= targets[i].radius) {
                    if (mode === 'breaking' && Math.abs(playerVx) > 0.2) {
                        score = Math.max(0, score - 50); showMovingError = true; errorTimer = 25;
                        return;
                    }
                    
                    // 연속 킬 및 콤보 보너스 시스템 작동
                    comboCount++;
                    comboTimer = 75; // 콤보 유지 제한 타이머 프레임 부여
                    score += 100 + (comboCount * 10);
                    hitAny = true;
                    
                    playValorantKillSound(comboCount); // 콤보 상승 변조 사운드 플레이
                    targets[i] = spawnBotData();
                    break;
                }
            }
            if (!hitAny) {
                score = Math.max(0, score - 20);
                comboCount = 0; // 빗나갈 시 콤보 리셋
            }
        }

        function loadLocalStorage() {
            if (localStorage.getItem('val_range_hs')) highScores = JSON.parse(localStorage.getItem('val_range_hs'));
            if (localStorage.getItem('val_range_sens')) {
                sensitivity = parseFloat(localStorage.getItem('val_range_sens'));
                document.getElementById('sens-slider').value = sensitivity;
                document.getElementById('sens-val').innerText = sensitivity.toFixed(2);
            }
            renderScoresUI();
        }

        function saveLocalStorage() { localStorage.setItem('val_range_hs', JSON.stringify(highScores)); }

        function updateSensitivity(val) {
            sensitivity = parseFloat(val);
            document.getElementById('sens-val').innerText = sensitivity.toFixed(2);
            localStorage.setItem('val_range_sens', sensitivity);
        }

        function renderScoresUI() {
            document.getElementById('record-board').innerHTML = `
                <div style="display:flex; justify-content:space-between; color:#4b5563; border-bottom:1px solid #1f2942; padding-bottom:4px; font-size:11px;">
                    <span>훈련 모드</span><span>최고 기록 스코어</span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-top:5px;">
                    <span style="color:${mode==='gridshot'?'#ff4655':'#9ca3af'}">🎯 GRIDSHOT</span><span style="font-weight:bold; color:#38bdf8;">${highScores.gridshot || 0}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span style="color:${mode==='tracking'?'#ff4655':'#9ca3af'}">🔄 TRACKING</span><span style="font-weight:bold; color:#00f2fe;">${highScores.tracking || 0}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span style="color:${mode==='microflex'?'#ff4655':'#9ca3af'}">⚡ MICROFLEX (Lvl 4완화)</span><span style="font-weight:bold; color:#f43f5e;">${highScores.microflex || 0}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span style="color:${mode==='breaking'?'#ff4655':'#9ca3af'}">💥 VAL-BREAKING</span><span style="font-weight:bold; color:#ff4655;">${highScores.breaking || 0}</span>
                </div>
            `;
        }

        function clearAllData() { highScores = { gridshot: 0, tracking: 0, microflex: 0, breaking: 0 }; saveLocalStorage(); renderScoresUI(); }

        function initBots() {
            targets = []; projectiles = [];
            let count = (mode === 'gridshot') ? 3 : 1;
            for(let i=0; i<count; i++) targets.push(spawnBotData());
            renderScoresUI();
        }

        function spawnBotData() {
            let baseRadius = 16; let baseSpeed = 2.5;
            if (mode === 'tracking') { baseRadius = 20; baseSpeed = 4.0; }
            else if (mode === 'microflex') { baseRadius = 12; baseSpeed = 3.2; } // 레벨 4 스펙 자동 적용 완화 규격 적용
            else if (mode === 'breaking') { baseRadius = 16; baseSpeed = 2.0; }

            return {
                x: 150 + Math.random() * (canvas.width - 300),
                y: 230 + Math.random() * (mode === 'breaking' ? 40 : 160),
                radius: baseRadius,
                vx: (Math.random() > 0.5 ? 1 : -1) * baseSpeed,
                vy: (mode === 'breaking' || mode === 'tracking') ? 0 : (Math.random() - 0.5) * baseSpeed
            };
        }

        function startRangeSession() {
            isPlaying = true; score = 0; timeLeft = 30.0; comboCount = 0; comboTimer = 0;
            playerX = 450; playerVx = 0; projectiles = []; enemyShootTimer = 0;
            initBots();
        }

        function quitRangeSession() {
            isPlaying = false; projectiles = []; comboCount = 0;
            initBots();
        }

        function endRangeSession() {
            isPlaying = false;
            if (score > (highScores[mode] || 0)) { highScores[mode] = score; saveLocalStorage(); }
            comboCount = 0; quitRangeSession();
        }

        function loop() {
            ctx.fillStyle = '#0b0e14'; ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // --- 구조물 및 발로란트 스타일 배경 가이드라인 디자인 ---
            ctx.fillStyle = '#111524'; ctx.fillRect(0, 0, canvas.width, 100); // 상단 전자 전광판 영역
            ctx.strokeStyle = '#223154'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(0,100); ctx.lineTo(canvas.width, 100); ctx.stroke();

            // 상단 메뉴 통합 사격판 드로잉 레이아웃
            uiTargets.forEach((ut) => {
                if (ut.id === 'quit_trigger' && !isPlaying) return; // 미작동 시 노출 차단
                
                let isCurrentMode = (ut.id === mode);
                ctx.save();
                if (ut.isAction) {
                    ctx.fillStyle = ut.id === 'start_trigger' ? (isPlaying ? '#374151' : '#047857') : '#b91c1c';
                } else {
                    ctx.fillStyle = isCurrentMode ? '#ff4655' : '#1f2942';
                }
                ctx.fillRect(ut.x, ut.y, ut.w, ut.h);
                
                ctx.strokeStyle = isCurrentMode ? '#ffffff' : '#4b5563';
                ctx.lineWidth = 1.5; ctx.strokeRect(ut.x, ut.y, ut.w, ut.h);
                
                ctx.fillStyle = '#ffffff'; ctx.font = 'bold 11px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
                ctx.fillText(ut.label, ut.x + ut.w/2, ut.y + ut.h/2);
                ctx.restore();
            });

            // 중앙 실시간 스코어보드 상황판 출력
            ctx.save();
            ctx.fillStyle = '#e5e7eb'; ctx.font = 'bold 16px monospace'; ctx.textAlign = 'center';
            if (isPlaying) {
                ctx.fillStyle = '#ff4655';
                ctx.fillText(`🎯 LIVE CHALLENGE | TIME: ${timeLeft.toFixed(1)}s | SCORE: ${score}`, canvas.width/2, 495);
            } else {
                ctx.fillStyle = '#6b7280';
                ctx.fillText(`[ 상단 대기판 사격: 현재 모드 - ${mode.toUpperCase()} ]`, canvas.width/2, 495);
            }
            ctx.restore();

            // 콤보 타이머 계산
            if (comboTimer > 0) { comboTimer--; if (comboTimer <= 0) comboCount = 0; }

            // 조준선 무빙 가속도 계산
            if (keys.a) playerVx = Math.max(-5.5, playerVx - 0.8);
            else if (keys.d) playerVx = Math.min(5.5, playerVx + 0.8);
            else { playerVx *= 0.6; }
            playerX = Math.max(50, Math.min(canvas.width - 50, playerX + playerVx));

            // 감도 필터링을 반영한 마우스 트랙 연동
            mouseX = rawMouseX; mouseY = rawMouseY;

            if (isPlaying) {
                timeLeft -= 1/60; if (timeLeft <= 0) { timeLeft = 0; endRangeSession(); }

                if (mode === 'tracking' && isMouseDown) {
                    targets.forEach((t) => {
                        let dist = Math.hypot(mouseX - t.x, mouseY - t.y);
                        if (dist <= t.radius) { score += 3; comboCount = 3; }
                    });
                }

                if (mode === 'breaking') {
                    enemyShootTimer++;
                    if (enemyShootTimer >= 45 && targets.length > 0) {
                        enemyShootTimer = 0; let t = targets[0];
                        let dx = playerX - t.x; let dy = (canvas.height - 35) - t.y; let dist = Math.hypot(dx, dy);
                        projectiles.push({ x: t.x, y: t.y, vx: (dx / dist) * 4.5, vy: (dy / dist) * 4.5, radius: 5 });
                    }
                }

                // 브레이킹 모드 투사체 연산처리
                for (let i = projectiles.length - 1; i >= 0; i--) {
                    let p = projectiles[i]; p.x += p.vx; p.y += p.vy;
                    if (p.y >= canvas.height - 40 && p.y <= canvas.height - 20) {
                        if (p.x >= playerX - 25 && p.x <= playerX + 25) {
                            score = Math.max(0, score - 60); projectiles.splice(i, 1); continue;
                        }
                    }
                    if (p.y > canvas.height) { projectiles.splice(i, 1); continue; }
                    ctx.fillStyle = '#f59e0b'; ctx.beginPath(); ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2); ctx.fill();
                }
            }

            // 과녁 훈련 봇 객체들 실시간 무빙 및 렌더링
            targets.forEach((t) => {
                if (isPlaying) {
                    t.x += t.vx; t.y += t.vy;
                    if (t.x - t.radius < 30 || t.x + t.radius > canvas.width - 30) t.vx *= -1;
                    if (t.y - t.radius < 120 || t.y + t.radius > 420) t.vy *= -1;
                }

                ctx.save();
                // 네온 스타일의 봇 원형 과녁 렌더링
                let grad = ctx.createRadialGradient(t.x, t.y, 2, t.x, t.y, t.radius);
                if (mode === 'gridshot') { grad.addColorStop(0, '#ffffff'); grad.addColorStop(1, '#38bdf8'); } 
                else if (mode === 'tracking') { grad.addColorStop(0, '#ffffff'); grad.addColorStop(1, '#00f2fe'); } 
                else if (mode === 'microflex') { grad.addColorStop(0, '#ffffff'); grad.addColorStop(1, '#f43f5e'); } 
                else { grad.addColorStop(0, '#ffffff'); grad.addColorStop(1, '#ff4655'); }
                
                ctx.fillStyle = grad; ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI * 2); ctx.fill();
                ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 1; ctx.stroke();
                ctx.restore();
            });

            // 움직임 오류 문구 출력
            if (showMovingError && errorTimer > 0) {
                ctx.save(); ctx.fillStyle = '#ff4655'; ctx.font = 'bold 18px sans-serif'; ctx.textAlign = 'center';
                ctx.fillText("❌ 만개 발생 (브레이킹 불완전 상태 사격 페널티)", canvas.width/2, 190); ctx.restore();
                errorTimer--; if(errorTimer <= 0) showMovingError = false;
            }

            // 하단 플레이어 컨트롤러 바
            ctx.fillStyle = Math.abs(playerVx) <= 0.2 ? '#22c55e' : '#eab308';
            ctx.fillRect(playerX - 25, canvas.height - 35, 50, 8);

            // 연속 콤보 킬수 텍스트 이펙트
            if (comboCount > 0) {
                ctx.save(); ctx.fillStyle = `rgba(255, 70, 85, ${comboTimer / 75})`; ctx.font = 'bold 24px sans-serif'; ctx.textAlign = 'center';
                ctx.fillText(`${comboCount} KILL COMBO!`, canvas.width/2, 450); ctx.restore();
            }

            // 리얼 FPS 정밀 십자선 (조준선 크로스헤어)
            ctx.save(); ctx.strokeStyle = '#ff4655'; ctx.lineWidth = 2;
            ctx.beginPath(); ctx.moveTo(mouseX - 8, mouseY); ctx.lineTo(mouseX + 8, mouseY); ctx.stroke();
            ctx.beginPath(); ctx.moveTo(mouseX, mouseY - 8); ctx.lineTo(mouseX, mouseY + 8); ctx.stroke();
            ctx.restore();

            requestAnimationFrame(loop);
        }

        loadLocalStorage(); initBots(); loop();
    </script>
    """
    st.components.v1.html(html_src, height=560)

if __name__ == "__main__":
    main()
