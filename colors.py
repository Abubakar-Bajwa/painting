import colorgram


def extract_colours(col_list):
    colors = colorgram.extract('painting.jpg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        col_list.append(new_color)
