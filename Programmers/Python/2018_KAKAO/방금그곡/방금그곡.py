def solution(m, musicinfos):
    answer = ["", ""]
    music_dic = {}

    m = m.replace('C#', 'c').replace('D#', 'd').replace(
        'F#', 'f').replace('G#', 'g').replace('A#', 'a')

    for music in musicinfos:
        start, end, title, code = music.split(',')
        # end = end.split(':')
        end = list(map(int, end.split(':')))
        # start = start.split(':')
        start = list(map(int, start.split(':')))
        # play_time = (int(end[0]) - int(start[0]))*60 + (int(end[1])-int(start[1]))
        play_time = (end[0]-start[0])*60 + (end[1]-start[1])
        code = code.replace('C#', 'c').replace('D#', 'd').replace(
            'F#', 'f').replace('G#', 'g').replace('A#', 'a')
        code = code*(play_time//len(code)) + code[:play_time % len(code)+1]
        music_dic[title] = code

    for title, code in music_dic.items():

        if m in code:
            if len(answer[1]) < len(code):

                answer[0] = title
                answer[1] = code

    return "(None)" if len(answer[0]) == 0 else answer[0]
