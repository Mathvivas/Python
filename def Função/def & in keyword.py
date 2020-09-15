def hat_av(color):
    hat_colors = "blue, green, red, orange"
    return(color.lower() in hat_colors)
have_hat = hat_av("Orange")
print(have_hat)
