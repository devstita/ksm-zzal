from PIL import Image, ImageFont, ImageDraw

def tuple_elementwise_calc(t1, t2, op):
    return tuple([op(x, y) for x, y in zip(t1, t2)])

def get_newlined_text_list(m, draw, font, max_width): 
    m_edit = m[:]
    while True: 
        text_width = draw.textsize(m_edit, font=font)[0]
        # print(m_edit)
        if text_width > max_width - 200:
            m_edit = m_edit[:-1]
        else:
            break
    
    if len(m_edit) == len(m): 
        return [m]
    else:
        return [m_edit, *get_newlined_text_list(m[len(m_edit):], draw, font, max_width)]
        

def create_image(m1, m2): 
    image = Image.open('templates/res/sungmo_origin.png')
    font = ImageFont.truetype('templates/res/NanumGothicBold.ttf', 60)
    image_width = image.size[0]
    draw = ImageDraw.Draw(image)

    m = [get_newlined_text_list(m1, draw, font, image_width), get_newlined_text_list(m2, draw, font, image_width)]
    sp_middle_coord = [(320.0, 155.0), (320.0, 820.0)]

    for i in range(2): 
        m_middle_coord = [tuple([x / 2 for x in draw.textsize(cur, font=font)]) for cur in m[i]]
        pos = tuple_elementwise_calc(sp_middle_coord[i], m_middle_coord[0], lambda a, b: a - b)
        pos = (pos[0], pos[1] - (draw.textsize('\n'.join(m[i]), font=font)[1] - draw.textsize(m[i][0], font=font)[1]) / 2)
        
        draw.text(pos, m[i][0], font=font, fill='#000000')
        for idx, line in enumerate(m[i][1:], 1): 
            pos = (tuple_elementwise_calc(sp_middle_coord[i], m_middle_coord[idx], lambda a, b: a - b)[0], pos[1] + draw.textsize(line, font=font)[1])
            draw.text(pos, m[i][idx], font=font, fill='#000000')
    
    return image

if __name__ == '__main__':
    create_image('사랑헤이요...', '연애가중계...').show() # About 50ms
