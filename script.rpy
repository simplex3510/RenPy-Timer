﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('수뭉이', color="#1fb8f5")

# 점수 변수 설정
default score = 0

# 화면에 점수 출력
screen score_display():
    text "Score: [score]" align (0.98, 0.02)  # 오른쪽 상단에 점수를 표시            

# 여기에서부터 게임이 시작합니다.
label start:

    # 점수 표시 화면을 항상 띄움
    show screen score_display

    "시작 전 안내사항 (대화창을 클릭할 시 다음으로 넘어갑니다.)"
    "플레이어가 선택하는 것에 따라 최종 점수 및 결과가 달라집니다."
    "진행 중 현재 점수는 우측 상단의 Score에서 확인할 수 있습니다."
    "게임을 시작합니다."
    scene black with dissolve

    e "맨날 과잠만 입고 있으니까 이젠 좀 질리네..."

    e "이번엔 기분전환도 할 겸, 학교 밖으로 나가 보는 거야!"

    e "그러려면 거기에 맞는 옷을 잘 골라 입어야겠지?"


# 아래로는 선택지입니다. 플레이어가 선택하는 것에 따라 최종 점수 및 결과가 달라집니다.
# 현재 점수변동 구현 중입니다.

menu:
    "어떤 장소로 갈까?"
    
    "클럽":
        e "그래! 가끔은 클럽에 가서 신나게 춤추다 오는 것도 좋지!"

        menu:
            "어떤 사람과 함께 갈까?"

            "가족":
                e "가족...이랑 클럽을 간다고? 뭐, 그럴 수 있지..." # 0점
                $ score += 0
                "점수에 변동이 없습니다."
                jump score_display

            "친구":
                e "좋아, 당장 친구한테 같이 가자고 연락해 봐야지!" # +3점
                $ score += 3
                "점수가 3점 올랐습니다."
                jump score_display

            "연인":
                e "으음... 말 꺼내면 큰일날 것 같은데. 그래, 같이 가서 즐겁게 놀다 오자고 해야지!" # 0점
                $ score += 0
                "점수에 변동이 없습니다."
                jump score_display

            "공적관계":
                e "뭐?" with vpunch
                e "...좋은 생각은 아닌 것 같아, 생각해보자... 교수님이랑 클럽...? 으음." # -3점
                $ score -= 3
                "점수가 3점 내려갔습니다."
                jump score_display

        label score_display:
            "현재 점수는 [score]점 입니다."
            # 필요한 다른 동작들 추가 가능

        menu :
            "오늘 날씨가 어떻지?"

            "맑음":
                e "날이 엄청 맑아! 햇빛도 좋고, 놀러가기 딱 좋은 날씨네." # +3점
                $ score += 3
                "점수가 3점 올랐습니다."
                "현재 점수는 [score]점 입니다."

            "흐림" :
                e "날이 조금 흐리긴 한데, 딱히 비나 눈이 올 것 같진 않아." # 0점
                "점수가 0점 올랐습니다."
                "점수에 변동이 없습니다."
                "현재 점수는 [score]점 입니다."

            "비" :
                e "모처럼 오랜만에 놀러가는데 하필이면 비가 오네." #-1점
                $ score -= 1
                "점수가 1점 내려갔습니다."
                "현재 점수는 [score]점 입니다."

            "눈" :
                e "엥! 벌써 눈이 온다고? 지구가 망하긴 했구나." #-1점
                $ score -= 1
                "점수가 1점 내려갔습니다."
                "현재 점수는 [score]점 입니다."                   
                
                return


    "도서관":
        e "오! 도서관에서 공부도 하고, 책도 읽으면 좋겠다."

        menu :
            "어떤 사람과 함께 갈까?"

            "가족" :
                e "가족이랑 도서관이라! 시간이 맞으려나." # 0점
            "친구" :
                e "전공 공부 같이 하자고 연락해 봐야겠다." # +3점
            "연인" :
                e "도서관 데이트 너무 좋지~" # 0점
            "공적관계" :
                e "모여서 팀플을 하는 것도 좋겠다." # +3점

                menu :
                    "오늘 날씨가 어떻지?"

                    "맑음" :
                        e "날이 엄청 맑아! 햇빛도 좋고, 따사롭게 공부에 집중할 수 있는 환경이겠다." # +3점
                    "흐림" :
                        e "날이 조금 흐리긴 한데, 딱히 비나 눈이 올 것 같진 않아." # 0점
                    "비" :
                        e "모처럼 오랜만에 도서관에 가는데 비가 오네. 흐리고 눅눅해서 별론데." # -1점
                    "눈" :
                        e "엥! 벌써 눈이 온다고? 지구가 망하긴 했구나." #-1점

    "술집":
        e "술 한 잔 하면서 피로를 푸는 것도 좋은 선택인 것 같아."

        menu :
            "어떤 사람과 함께 갈까?"

            "가족" :
                e "가족이 다 같이 모여서 술 한 잔 하는 것도 좋지. 아 나 근데 우리 아빠 감당 안 되는데..." # 0점
            "친구" :
                e "ㅇ"
            "연인" :
                e "d"
            "공적관계" :
                e "d"

    "카페":
        e "헉! 수업때문에 테이크아웃은 자주 해봤는데, 매장을 이용하는 건 오랜만이야."
