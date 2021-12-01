from PIL import Image, ImageFont, ImageDraw

def get_newlined_text(m, draw, font, max_width): 
    m_edit = m[:]
    while True: 
        text_width = draw.textsize(m_edit, font=font)[0]
        print(m_edit)
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
    width = image.size[0]
    draw = ImageDraw.Draw(image)

    m1 = get_newlined_text(m1, draw, font, width)
    m2 = get_newlined_text(m2, draw, font, width)

    print(m1)
    print('====')
    print(m2)
    
    draw.text(((width - draw.textsize(m1, font=font)[0]) / 2, 140), m1, font=font, fill='#000000')
    draw.text(((width - draw.textsize(m2, font=font)[0]) / 2, 400), m2, font=font, fill='#000000')
    image.show()

create_image('XX가...', '말대꾸대대대대꾸대꾸꾸꾸?!')
