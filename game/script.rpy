# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




define me = Character("恵", image = "me")
define to = Character("倫也", image = "to")
define mi = Character("美玖", image = "mi")
define yarou = Character("野郎", image = "yarou")
define cop = Character("警察官")
define sensei = Character("先生")
define mom = Character("恵の母")
define Left = Position(xpos= 0.25, ypos = 0.75)
define Right = Position(xpos = 0.75, ypos = 0.75)
define transition = Dissolve(0.5)
define slowTransition = Dissolve(1.0)


transform slightleft:
    xalign 0.25
    yalign 1.0


transform default:
    xalign 0.5
    yalign 1.0

label start :
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.RRRR
    play music "LikeTheWind.mp3"
    
    scene bg room
    with Dissolve(5.0)



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show tomoya normal at truecenter with annoytheuser
    to "やっと高校生になったな。時間が早すぎる."
    hide tomoya

    show megumi happy at truecenter with Dissolve(5.0)
    me "倫也君、お久しぶり！ともやくんも戸山高校に通ってたんだ."
    hide megumi

    show tomoya happy at truecenter with transition
    to "本当に久しぶりだな.８年ぶりじゃん."
    hide tomoya

    show miku normal at truecenter with transition
    mi "と。。ともやくん！お久しぶりですね！今年もよろしくお願いします。"
    hide miku
    
    show tomoya happy at truecenter with transition
    to "え？小学校の時の美玖Rじゃん！おれ、小学校だけ、千葉だったけど、みくはまだ千葉に住んでいると思ったよ。"
    hide tomoya

    show miku normal at truecenter with transition
    mi "うん、引っ越したばっかりですよ。ともや君と同じクラスになって、う、う。。嬉しいよ！"
    hide miku

    show tomoya happy at truecenter with transition
    to "こちらも同じだ！よろしくな！"
    to "あ、なんか二人の知り合いと一緒のクラスになるなんて、まるで運命だよ！最高のひだ！"
    to "みく、こちらはめぐみ、僕の幼馴染だ！子供の時はずっと一緒に遊んでたんだ！"
    to "こちらは　美玖、僕の小学校の友達だ！二人とも、仲良くしてほしいな！"
    hide tomoya

    show miku normal at Left with transition
    show megumi happy at Right with transition
    "よろしくおねがいします！"
label scene2:
    scene bg after_school 
    with Dissolve(3.0)

    show miku normal at truecenter with fade
    mi "そろそろ帰る時間だな。早く家に帰って、お風呂に入って、すきな番組をみようか～。。。ああ、いけない！今日はバイトがあるんだった。。。まったく、休もうと思ったのに。。。"
    mi "仕方ないな。。じゃ、さっそくバイトのところに行こうか！"
    hide miku
    "（人たちが歩いている音。。。)"
    show gang normal at truecenter with transition
    yarou "な～、一人きりか？おれたちと遊ばない？たのしいぜ！"
    hide gang

    show miku normal at truecenter with transition
    mi "すみません。今時間がないので。。"
    hide miku

    show gang normal at truecenter with transition
    yarou "ちょっとだから、平気だよ、平気！。。。
    （ほかの野郎：すげえ美人だ！）"
    hide gang

    show miku normal at truecenter with transition
    mi "でも。。。でも。。"
    hide miku

    show gang normal at truecenter with transition
    yarou "いいから、付き合ってくれよ、かわいい子ちゃん！（美玖の手を繋ぐ）"
    hide gang

    show miku normal at truecenter with transition
    mi "（誰か。。。たすけて！！）"
    hide miku

    show tomoya happy at truecenter with transition
    to "離せ。。。俺(おれ)の彼女だ。。。"
    hide tomoya

    show gang normal at truecenter with transition
    yarou "クソガキ！喧嘩をふっかけたいか。。。"
    hide gang

    to "（パンチの音)"

    show tomoya happy at truecenter with transition
    to "離せってば！"
    hide tomoya    

    show gang normal at truecenter with transition
    yarou "死にたいのか、くそがき！お前ら、こいつをやっちまおうぜ！"
    hide gang
    "（殴るおと。。。)"

    show miku normal at truecenter with transition
    mi "やめて！やめてください、おねがい！"
    hide miku
    "(警察の車の音。。。)"
    cop "逮捕する！動くな！"

    show tomoya happy at truecenter with transition
    to "（やっと警察が来たか。。。ちょっとおそいな。。。）"
    hide tomoya   


    show gang normal at truecenter with transition
    yarou "やべー！逃げよう、お前ら！ (警察に追い出される。。。）"
    hide gang

    show miku normal at truecenter with transition
    mi "ともやくん、ともやくん！だいじょうぶの？？"
    hide miku

    show tomoya happy at truecenter with transition
    to "平気だよ、このぐらいの傷。美玖が無事で、よかった！"
    hide tomoya   

    show miku normal at truecenter with transition
    mi "ともや。。。本当にありがとうございます。ともや君が助けてくれなかったら。。。"
    hide miku

    show tomoya happy at truecenter with transition
    to "気にしないで！ただとうぜんのことをしただけだから！"
    hide tomoya  

label scene3:
    scene bg classroom
    show tomoya happy at truecenter 
    with Dissolve(1.0)
    to "(変だな。。。どうして恵ちゃんは学校にいないんだろう。。。先生にきいてみようか.）"
    to "先生、どうして今日は恵さんが学校に来ないんですか？"
    hide tomoya
    sensei "そうですね。実は恵さんから連絡がないので，よく分かりません。"

    show tomoya happy at truecenter with transition
    to "そうですか？ありがとうございます！"
    hide tomoya

    pause 1.0
    
    scene bg house
    with Dissolve(2.0)

    narrator "(放課後に。。。)" # NO VOICEOVER

    show tomoya happy at truecenter with transition
    to "すみません、恵さんはいますか？お見舞いにきたんですが。。"
    hide tomoya
 
    mom "あ、ともや君、久しぶりね！どうぞ、入って！恵は部屋にいるんのよ。"
    
    show tomoya happy at truecenter with transition
    to "お邪魔します！"
    hide tomoya 

    scene bg megumi_room
    
    show megumi happy at truecenter with transition
    me "（恥ずかしくなる恵）ともやくん！？どうしてここに。。。"
    hide megumi

    show tomoya happy at truecenter with transition
    to "お見舞いに来たよ。朝から恵ちゃんの姿が見えなくて、先生にきいてもぜんぜん君の状態を知らなかったんだ！"
    hide tomoya   

    show megumi happy at truecenter with transition
    me "じゃ、どうやってあたしが病気になったのを知っているの？。。。"
    hide megumi



    # This ends the game.

return
