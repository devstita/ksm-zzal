from PIL import Image, ImageFont, ImageDraw

def tuple_elementwise_calc(t1, t2, op):
    return tuple([op(x, y) for x, y in zip(t1, t2)])

def get_newlined_text(m, draw, font, max_width): 
    m_edit = m[:]
    while True: 
        text_width = draw.textsize(m_edit, font=font)[0]
        # print(m_edit)
        if text_width > max_width - 200:
            m_edit = m_edit[:-1]
        else:
            break
    
    if len(m_edit) == len(m): 
        return m
    else:
        return m_edit + '\n' + m[len(m_edit):]
        

def create_image(m1, m2): 
    image = Image.open('templates/res/sungmo_origin.png')
    font = ImageFont.truetype('templates/res/NanumGothicBold.ttf', 60)
    image_width = image.size[0]
    draw = ImageDraw.Draw(image)

    m1 = get_newlined_text(m1, draw, font, image_width)
    m2 = get_newlined_text(m2, draw, font, image_width)

    sp_middle_coord = [(320.0, 157.5), (320.0, 825.0)]
    m_middle_coord = [tuple([x / 2 for x in draw.textsize(m1, font=font)]), tuple([x / 2 for x in draw.textsize(m2, font=font)])]

    draw.text(tuple_elementwise_calc(sp_middle_coord[0], m_middle_coord[0], lambda a, b: a - b), m1, font=font, fill='#000000')
    draw.text(tuple_elementwise_calc(sp_middle_coord[1], m_middle_coord[1], lambda a, b: a - b), m2, font=font, fill='#000000')
    image.show()

create_image('지명이가...', '말대꾸?!')
