import streamlit as st
import time

def main():
    st.set_page_config(page_title="VALORANT CHAMPIONS SKIN SHOWCASE", layout="wide")

    # 🎨 챔피언스 특유의 다크 VCT 레드 & 골드 테마 스타일링
    st.markdown("""
        <style>
        .main { background-color: #0d0e12; color: #ece8e1; font-family: 'Bourgeois', 'Segoe UI', sans-serif; }
        .stButton > button {
            background: linear-gradient(135deg, #bd9244 0%, #8a662d 100%) !important;
            color: #0d0e12 !important; font-weight: bold !important; border: 1px solid #bd9244 !important; 
            padding: 12px; border-radius: 4px; width: 100%; letter-spacing: 1px;
        }
        .stButton > button:hover {
            background: #ece8e1 !important; color: #0d0e12 !important; border: 1px solid #ece8e1 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center; color:#bd9244; font-weight:900; letter-spacing:2px;'>🏆 VCT CHAMPIONS SKIN SHOWCASE</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#76808c; font-size:14px;'>챔피언스 시리즈 특유의 황금빛 오라와 전용 재장전, 칼 검사(Inspect) 애니메이션 엔진</p>", unsafe_allow_html=True)

    html_src = """
    <div style="max-width:1050px; margin:0 auto;">
        <div style="display:flex; gap:15px; margin-bottom:15px; justify-content:center;">
            <button onclick="selectWeapon('vandal')" style="background:#1f222b; color:#bd9244; border:2px solid #bd9244; padding:10px 25px; font-weight:bold; cursor:pointer; border-radius:4px;" id="btn-vandal">💥 챔피언스 밴달</button>
            <button onclick="selectWeapon('karambit')" style="background:#14161d; color:#8a8f98; border:1px solid #2f3441; padding:10px 25px; font-weight:bold; cursor:pointer; border-radius:4px;" id="btn-karambit">🔪 챔피언스 카람빗</button>
            <button onclick="selectWeapon('kunai')" style="background:#14161d; color:#8a8f98; border:1px solid #2f3441; padding:10px 25px; font-weight:bold; cursor:pointer; border-radius:4px;" id="btn-kunai">📐 챔피언스 쿠나이</button>
        </div>

        <div style="display:flex; gap:20px;">
            <canvas id="skinCanvas" width="720" height="460" style="background:#111217; border:2px solid #2f3441; border-radius:6px;"></canvas>
            
            <div style="width:290px; background:#1f222b; padding:18px; border-radius:6px; border:1px solid #2f3441; display:flex; flex-direction:column; gap:12px;">
                <span style="color:#bd9244; font-size:13px; font-weight:bold; letter-spacing:1px;">🕹️ SKIN INTERACTION</span>
                
                <button onclick="triggerInspect()" style="background:#bd9244; color:#0d0e12; border:none; padding:12px; border-radius:4px; font-weight:bold; cursor:pointer; font-size:14px;">🔍 무기 자세히 보기 (Y)</button>
                <button id="action-btn" onclick="triggerAction()" style="background:#ece8e1; color:#0d0e12; border:none; padding:12px; border-radius:4px; font-weight:bold; cursor:pointer; font-size:14px;">🔥 무기 발사 (L-Click)</button>
                
                <hr style="border:0; border-top:1px solid #2f3441; margin:5px 0;">
                
                <span style="color:#bd9244; font-size:13px; font-weight:bold;">✨ CHAMPIONS AURA</span>
                <div style="display:flex; justify-content:between; align-items:center; background:#111217; padding:10px; border-radius:4px;">
                    <span style="font-size:12px; color:#8a8f98;">탑 킬러 오라 이펙트</span>
                    <button onclick="toggleAura()" id="aura-status" style="background:#ff4655; color:white; border:none; padding:4px 10px; border-radius:2px; cursor:pointer; font-size:11px; font-weight:bold;">OFF</button>
                </div>

                <div style="background:#111217; padding:12px; border-radius:4px; margin-top:auto; font-family:monospace; font-size:12px; border-left:4px solid #bd9244;">
                    <div style="color:#bd9244; font-weight:bold; margin-bottom:5px;">🔊 SFX FEEDBACK LOG</div>
                    <div id="sfx-log" style="color:#ece8e1; height:80px; overflow-y:auto; display:flex; flex-direction:column-reverse; gap:4px;">
                        <div style="color:#64748b;">[시스템] 챔피언스 컬렉션 로드 완료.</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('skinCanvas');
        const ctx = canvas.getContext('2d');

        let currentWeapon = 'vandal';
        let isInspect = false;
        let isAction = false;
        let auraActive = false;
        
        let animFrame = 0;
        let actionFrame = 0;
        let particles = [];

        function logSFX(msg) {
            const log = document.getElementById('sfx-log');
            const div = document.createElement('div');
            div.innerHTML = msg;
            log.insertBefore(div, log.firstChild);
        }

        function selectWeapon(type) {
            currentWeapon = type;
            isInspect = false;
            isAction = false;
            animFrame = 0;
            actionFrame = 0;
            
            // UI 버튼 활성화 스타일 전환
            ['vandal', 'karambit', 'kunai'].forEach(w => {
                const btn = document.getElementById('btn-' + w);
                if(w === type) {
                    btn.style.background = '#1f222b';
                    btn.style.border = '2px solid #bd9244';
                    btn.style.color = '#bd9244';
                } else {
                    btn.style.background = '#14161d';
                    btn.style.border = '1px solid #2f3441';
                    btn.style.color = '#8a8f98';
                }
            });

            const actBtn = document.getElementById('action-btn');
            if(type === 'vandal') {
                actBtn.innerText = "🔥 무기 발사 (L-Click)";
                logSFX("<span style='color:#bd9244;'>🎵 [SFX] 챔피언스 밴달 장착 (스킨 고유 음악 루프 오프닝)</span>");
            } else {
                actBtn.innerText = "⚡ 근접무기 공격 (L-Click)";
                logSFX("<span style='color:#bd9244;'>🎵 [SFX] 근접무기 스왑 (슉- 서너번 돌아가는 고유 사운드)</span>");
            }
        }

        function triggerInspect() {
            isInspect = true;
            animFrame = 0;
            if(currentWeapon === 'vandal') {
                logSFX("🔍 <span style='color:#ece8e1;'>[Inspect] 밴달을 들어올리며 챔피언스 VCT 메인 테마곡 재생</span>");
            } else if(currentWeapon === 'karambit') {
                logSFX("🔍 <span style='color:#ece8e1;'>[Inspect] 손가락에 걸고 카람빗 무한 고속 회전 연출 개시</span>");
            } else {
                logSFX("🔍 <span style='color:#ece8e1;'>[Inspect] 쿠나이를 허공에 띄워 골드 마법진 형상화 모션 재생</span>");
            }
        }

        function triggerAction() {
            isAction = true;
            actionFrame = 0;
            if(currentWeapon === 'vandal') {
                logSFX("💥 <span style='color:#ff4655;'>[SFX] 탕! 탕! 챔피언스 헤비 플래시 격발음 (VCT 킬 비주얼 연동)</span>");
                // 격발 플래시 파티클
                for(let i=0; i<8; i++){
                    particles.push({x: 520, y: 200, vx: Math.random()*5+2, vy: (Math.random()-0.5)*4, color: '#bd9244', size: Math.random()*4+2, life: 1});
                }
            } else {
                logSFX("⚔️ <span style='color:#38bdf8;'>[SFX] 슥- 삭! 공간을 가르는 골드 슬래시 궤적음</span>");
            }
        }

        function toggleAura() {
            auraActive = !auraActive;
            const btn = document.getElementById('aura-status');
            if(auraActive) {
                btn.innerText = "ON";
                btn.style.background = "#22c55e";
                logSFX("<span style='color:#22c55e; font-weight:bold;'>✨ [AURA] 최다 킬러 달성 - 무기 주변 황금빛 불꽃 오라 활성화</span>");
            } else {
                btn.innerText = "OFF";
                btn.style.background = "#ff4655";
                logSFX("<span style='color:#ff4655;'>✨ [AURA] 오라 비활성화</span>");
            }
        }

        function drawWeaponBase(x, y, scale, angle) {
            ctx.save();
            ctx.translate(x, y);
            ctx.rotate(angle);

            // 챔피언스 오라 효과 버프 렌더링
            if (auraActive) {
                ctx.save();
                ctx.shadowBlur = 25;
                ctx.shadowColor = '#bd9244';
                ctx.strokeStyle = 'rgba(189, 146, 68, 0.4)';
                ctx.lineWidth = 6;
                if(currentWeapon === 'vandal') {
                    ctx.strokeRect(-160, -25, 320, 50);
                } else {
                    ctx.beginPath(); ctx.arc(0, 0, 60, 0, Math.PI*2); ctx.stroke();
                }
                ctx.restore();
            }

            // 각 스킨별 벡터 아웃라인 외관 자세히 보기 뼈대 구현
            if(currentWeapon === 'vandal') {
                // 몸체 VCT 시그니처 깨진 각진 패턴 바디
                ctx.fillStyle = '#1c1e24';
                ctx.fillRect(-150, -20, 260, 35);
                ctx.fillStyle = '#0d0e12';
                ctx.fillRect(-60, -15, 120, 25);
                
                // 골드 챔피언스 라인 인레이 디자인
                ctx.fillStyle = '#bd9244';
                ctx.beginPath();
                ctx.moveTo(-100, -20); ctx.lineTo(-40, -5); ctx.lineTo(-120, 15);
                ctx.fill();

                // 총열 및 개머리판
                ctx.fillStyle = '#2f3441';
                ctx.fillRect(110, -10, 80, 12); // 바렐
                ctx.fillRect(-200, -20, 50, 45); // 스톡
                
                // VCT 로고 센터 인레이
                ctx.fillStyle = '#ff4655';
                ctx.beginPath();
                ctx.moveTo(0, -5); ctx.lineTo(10, 10); ctx.lineTo(-10, 10);
                ctx.fill();

            } else if(currentWeapon === 'karambit') {
                // 고리형 카람빗 단검 아웃라인
                ctx.strokeStyle = '#bd9244';
                ctx.lineWidth = 5;
                ctx.fillStyle = '#1c1e24';
                
                // 손잡이 및 링
                ctx.beginPath();
                ctx.arc(-40, 0, 18, 0, Math.PI*2);
                ctx.stroke(); ctx.fill();
                
                // 칼날 챔피언스 독창적 곡선 낫 모양
                ctx.fillStyle = '#0d0e12';
                ctx.beginPath();
                ctx.moveTo(-20, -5);
                ctx.quadraticCurveTo(30, -40, 70, -10);
                ctx.quadraticCurveTo(30, 15, -20, 15);
                ctx.closePath();
                ctx.fill();
                ctx.stroke();

                // 칼날 안쪽 골드 인레이 기하학 문양
                ctx.fillStyle = '#bd9244';
                ctx.beginPath();
                ctx.moveTo(10, -15); ctx.lineTo(40, -22); ctx.lineTo(25, -5);
                ctx.fill();

            } else if(currentWeapon === 'kunai') {
                // 밸런스 잡힌 직선형 대칭 쿠나이 디자인
                ctx.strokeStyle = '#2f3441';
                ctx.lineWidth = 3;
                
                // 손잡이 링
                ctx.fillStyle = '#1c1e24';
                ctx.beginPath(); ctx.arc(-70, 0, 12, 0, Math.PI*2); ctx.fill(); ctx.stroke();
                // 핸들 그립
                ctx.fillRect(-58, -5, 58, 10);

                // 마법 단검 대칭 블레이드
                ctx.fillStyle = '#0d0e12';
                ctx.beginPath();
                ctx.moveTo(0, -25);
                ctx.lineTo(80, 0);
                ctx.lineTo(0, 25);
                ctx.closePath();
                ctx.fill();
                
                // 중앙을 가르는 골드 레이저 음각선
                ctx.fillStyle = '#bd9244';
                ctx.fillRect(0, -3, 60, 6);
            }

            ctx.restore();
        }

        function loop() {
            // 배경 그리드 패턴 드로우
            ctx.fillStyle = '#111217';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.strokeStyle = '#1a1c23'; ctx.lineWidth = 1;
            for(let i=0; i<canvas.width; i+=50) {
                ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); ctx.stroke();
            }

            // 센터 타겟 기준좌표 세팅
            let cx = canvas.width / 2;
            let cy = canvas.height / 2;
            let targetAngle = 0;
            let targetScale = 1.0;

            // 1️⃣ 무기 자세히 보기 (Inspect) 애니메이션 각도/위치 수식 연산
            if (isInspect) {
                animFrame++;
                if(currentWeapon === 'vandal') {
                    // 회전했다가 다시 정위치로 오는 모션
                    targetAngle = Math.sin((animFrame / 120) * Math.PI) * 0.25;
                    cy += Math.sin((animFrame / 60) * Math.PI) * 15;
                    if(animFrame > 120) isInspect = false;
                } else if(currentWeapon === 'karambit') {
                    // 카람빗 손가락 무한 360도 고속 회전 고증 메커니즘
                    targetAngle = (animFrame * 0.18);
                    if(animFrame > 180) isInspect = false;
                } else if(currentWeapon === 'kunai') {
                    // 공중에 붕 떠올라 가볍게 앞뒤로 흔들리는 신비로운 연출
                    cy -= 30 * Math.sin((animFrame / 90) * Math.PI);
                    targetAngle = Math.sin((animFrame / 45) * Math.PI) * 0.1;
                    if(animFrame > 180) isInspect = false;
                }
            }

            // 2️⃣ 무기 격발/공격(Action) 애니메이션 연산
            if (isAction) {
                actionFrame++;
                if(currentWeapon === 'vandal') {
                    // 리얼한 총기 반동 후퇴거리 수식 구현
                    cx -= 12 * Math.exp(-actionFrame * 0.2);
                    if(actionFrame > 15) isAction = false;
                } else {
                    // 나이프 근접 공격 시 전방으로 휙 베어내는 아크 궤적 연산
                    targetAngle = Math.sin((actionFrame / 20) * Math.PI) * 0.8;
                    cx += 30 * Math.sin((actionFrame / 20) * Math.PI);
                    if(actionFrame > 20) isAction = false;
                }
            }

            // 파티클 시스템 업데이트 및 드로우
            for(let i=particles.length-1; i>=0; i--) {
                let p = particles[i];
                p.x += p.vx; p.y += p.vy; p.life -= 0.05;
                if(p.life <= 0) { particles.splice(i, 1); continue; }
                ctx.fillStyle = p.color;
                ctx.globalAlpha = p.life;
                ctx.beginPath(); ctx.arc(p.x, p.y, p.size, 0, Math.PI*2); ctx.fill();
                ctx.globalAlpha = 1.0;
            }

            // 최종 무기 렌더링 호출
            drawWeaponBase(cx, cy, targetScale, targetAngle);

            // 가이드 UI 텍스트 오버레이
            ctx.fillStyle = '#64748b'; ctx.font = '11px sans-serif'; ctx.textAlign = 'left';
            ctx.fillText("VCT CHAMPIONS SPECIAL SYSTEM PROTOTYPE v2", 20, canvas.height - 20);

            requestAnimationFrame(loop);
        }

        // 초기 구동 첫 셋업 활성화
        selectWeapon('vandal');
        loop();
    </script>
    """
    st.components.v1.html(html_src, height=520)

if __name__ == "__main__":
    main()
