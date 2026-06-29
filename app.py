import streamlit as st

def main():
    st.set_page_config(page_title="TACTICAL AIM TRAINER PRO", layout="wide")

    # 🎨 오직 에임에만 집중할 수 있는 깔끔한 다크 테마
    st.markdown("""
        <style>
        .main { background-color: #0b0c10; color: #c5c6c7; font-family: 'Segoe UI', monospace; }
        .stButton > button {
            background: linear-gradient(135deg, #45f3ff, #1f51ff) !important;
            color: #000000 !important; font-weight: bold !important; border: none !important;
            padding: 10px 20px; border-radius: 4px; width: 100%; transition: 0.2s;
        }
        .stButton > button:hover {
            box-shadow: 0 0 15px #45f3ff; transform: scale(1.01);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center; color:#45f3ff; font-weight:800; letter-spacing:1px;'>🎯 TACTICAL AIM LAB PRO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; font-size:14px;'>불필요한 그래픽을 배제한 순수 에임 트레이닝 및 메커니즘 측정 엔진</p>", unsafe_allow_html=True)

    html_src = """
    <div style="max-width:1100px; margin:0 auto; text-align:center;">
        <div style="display:flex; justify-content:space-between; align-items:center; background:#1f2833; padding:12px 24px; border-radius:6px; margin-bottom:15px; border:1px solid #45f3ff;">
            <div style="display:flex; gap:10px;">
                <button onclick="setMode('gridshot')" id="m-grid" style="background:#45f3ff; color:black; border:none; padding:8px 16px; font-weight:bold; cursor:pointer; border-radius:4px;">🎯 GRIDSHOT</button>
                <button onclick="setMode('tracking')" id="m-track" style="background:#0b0c10; color:#45f3ff; border:1px solid #45f3ff; padding:8px 16px; font-weight:bold; cursor:pointer; border-radius:4px;">🔄 TRACKING</button>
            </div>
            <div style="display:flex; gap:25px; font-family:monospace; font-size:16px; font-weight:bold;">
                <div style="color:#45f3ff;" id="ui-score">SCORE: 0</div>
                <div style="color:#66fcf1;" id="ui-acc">ACCURACY: 100%</div>
                <div style="color:#ff4545;" id="ui-time">TIME: 30.0s</div>
            </div>
            <div>
                <button onclick="resetTraining()" style="background:#ff4545; color:white; border:none; padding:8px 16px; font-weight:bold; cursor:pointer; border-radius:4px;">RESET</button>
            </div>
        </div>

        <canvas id="aimCanvas" width="900" height="540" style="background:#121212; border:2px solid #1f2833; border-radius:6px; cursor:none;"></canvas>
    </div>

    <script>
        const canvas = document.getElementById('aimCanvas');
        const ctx = canvas.getContext('2d');

        // 시스템 상태 변수
        let mode = 'gridshot'; // 'gridshot' 또는 'tracking'
        let isRunning = false;
        let score = 0;
        let timeLeft = 30.0;
        let totalShots = 0;
        let hitShots = 0;
        let mouseX = 450, mouseY = 270;

        // 타겟 데이터 배열 (그리드샷은 여러 개, 트래킹은 1개 사용)
        let targets = [];

        function setMode(m) {
            mode = m;
            document.getElementById('m-grid').style.background = (m === 'gridshot') ? '#45f3ff' : '#0b0c10';
            document.getElementById('m-grid').style.color = (m === 'gridshot') ? 'black' : '#45f3ff';
            document.getElementById('m-track').style.background = (m === 'tracking') ? '#45f3ff' : '#0b0c10';
            document.getElementById('m-track').style.color = (m === 'tracking') ? 'black' : '#45f3ff';
            resetTraining();
        }

        function createTarget() {
            let t = {
                x: 60 + Math.random() * (canvas.width - 120),
                y: 60 + Math.random() * (canvas.height - 120),
                radius: mode === 'gridshot' ? 20 : 25,
                // 트래킹 모드용 속도 벡터
                vx: (Math.random() - 0.5) * 5,
                vy: (Math.random() - 0.5) * 5
            };
            return t;
        }

        function resetTraining() {
            score = 0;
            timeLeft = 30.0;
            totalShots = 0;
            hitShots = 0;
            isRunning = true;
            targets = [];

            if (mode === 'gridshot') {
                // 화면에 상시 3개의 타겟 유지
                for(let i=0; i<3; i++) targets.push(createTarget());
            } else {
                // 트래킹은 움직이는 타겟 1개
                targets.push(createTarget());
            }
            updateDashboard();
        }

        function updateDashboard() {
            document.getElementById('ui-score').innerText = "SCORE: " + score;
            let acc = totalShots > 0 ? Math.round((hitShots / totalShots) * 100) : 100;
            document.getElementById('ui-acc').innerText = "ACCURACY: " + acc + "%";
            document.getElementById('ui-time').innerText = "TIME: " + timeLeft.toFixed(1) + "s";
        }

        // 마우스 무브 이벤트 연동
        canvas.addEventListener('mousemove', (e) => {
            let rect = canvas.getBoundingClientRect();
            mouseX = (e.clientX - rect.left) * (canvas.width / rect.width);
            mouseY = (e.clientY - rect.top) * (canvas.height / rect.height);
        });

        // 마우스 클릭 (격발 판정)
        canvas.addEventListener('mousedown', () => {
            if (!isRunning) {
                resetTraining(); // 끝났을 때 클릭하면 재시작
                return;
            }

            totalShots++;
            let hitAny = false;

            for (let i = 0; i < targets.length; i++) {
                let dist = Math.hypot(mouseX - targets[i].x, mouseY - targets[i].y);
                if (dist <= targets[i].radius) {
                    hitShots++;
                    score += 100;
                    hitAny = true;
                    
                    if (mode === 'gridshot') {
                        targets[i] = createTarget(); // 맞춘 타겟은 즉시 무작위 재생성
                    }
                    break;
                }
            }

            if (!hitAny && mode === 'gridshot') {
                score = Math.max(0, score - 30); // 빗나감 감점 (그리드샷 전용)
            }
            updateDashboard();
        });

        function renderLoop() {
            // 배경 청소 및 깔끔한 매트 차콜 톤 바닥
            ctx.fillStyle = '#121212';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // 보이지 않는 격자선 가이드라인
            ctx.strokeStyle = '#1a1a1a'; ctx.lineWidth = 1;
            for(let i=0; i<canvas.width; i+=60) { ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,canvas.height); ctx.stroke(); }

            if (isRunning) {
                // 시간 감소 처리
                timeLeft -= 1/60;
                if (timeLeft <= 0) {
                    timeLeft = 0;
                    isRunning = false;
                }
                updateDashboard();

                // 모드별 타겟 물리 연산 및 렌더링
                targets.forEach((t) => {
                    if (mode === 'tracking') {
                        // 트래킹 모드: 매 프레임 벽 충돌 및 이동 연산
                        t.x += t.vx;
                        t.y += t.vy;
                        if (t.x - t.radius < 0 || t.x + t.radius > canvas.width) t.vx *= -1;
                        if (t.y - t.radius < 0 || t.y + t.radius > canvas.height) t.vy *= -1;

                        // 마우스가 실시간으로 원 안에 머물러 있는지 체크 (트래킹 점수 부여 방식)
                        let dist = Math.hypot(mouseX - t.x, mouseY - t.y);
                        if (dist <= t.radius) {
                            score += 1; // 유지 시 점수 누적 증가
                        }
                    }

                    // 🎯 프로급 조준용 하이테크 원형 타겟 디자인 (네온 사이언 컬러)
                    ctx.save();
                    ctx.strokeStyle = '#45f3ff';
                    ctx.lineWidth = 3;
                    ctx.beginPath(); ctx.arc(t.x, t.y, t.radius, 0, Math.PI*2); ctx.stroke();
                    
                    // 내부 중심 도트
                    ctx.fillStyle = '#45f3ff';
                    ctx.beginPath(); ctx.arc(t.x, t.y, 4, 0, Math.PI*2); ctx.fill();
                    ctx.restore();
                });
            } else {
                // 종료 및 대기 화면 안내 메세지
                ctx.fillStyle = '#ffffff';
                ctx.font = 'bold 20px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('TRAINING SELECTION READY', canvas.width/2, canvas.height/2 - 20);
                ctx.fillStyle = '#666';
                ctx.font = '14px sans-serif';
                ctx.fillText('화면을 클릭하거나 상단의 RESET 버튼을 누르면 시작합니다.', canvas.width/2, canvas.height/2 + 15);
            }

            // 🛠️ 정밀 십자선 크로스헤어 (정밀 사격용 도트 융합형)
            ctx.save();
            ctx.strokeStyle = '#66fcf1';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(mouseX - 10, mouseY); ctx.lineTo(mouseX - 2, mouseY);
            ctx.moveTo(mouseX + 2, mouseY); ctx.lineTo(mouseX + 10, mouseY);
            ctx.moveTo(mouseX, mouseY - 10); ctx.lineTo(mouseX, mouseY - 2);
            ctx.moveTo(mouseX, mouseY + 2); ctx.lineTo(mouseX, mouseY + 10);
            ctx.stroke();
            ctx.restore();

            requestAnimationFrame(renderLoop);
        }

        // 초기 시작 가동
        setMode('gridshot');
        renderLoop();
    </script>
    """
    st.components.v1.html(html_src, height=620)

if __name__ == "__main__":
    main()
