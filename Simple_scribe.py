# Create a function which edits the text style
def style_text(string,style_code):
    
    # store styles in variables
    OFF = "\033[0m"
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    RED = "\033[91m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    
    # apply the appropriate styling to the text
    if style_code == '<B>':
        formatted_string = f"{BOLD}{string}{OFF}"
    elif style_code == "<i>":
        formatted_string = f"{ITALIC}{string}{OFF}"
    elif style_code == "<u>":
        formatted_string = f"{UNDERLINE}{string}{OFF}"
    elif style_code == "<r>":
        formatted_string = f"{RED}{string}{OFF}"
    elif style_code == "<g>":
        formatted_string = f"{GREEN}{string}{OFF}"
    elif style_code == "<b>":
        formatted_string = f"{BLUE}{string}{OFF}"
        
    return formatted_string

# user types in their text, for now, hard code text whilst coding
print("\033[1;4mWELCOME TO SIMPLE SCRIBE\033[0m")
print("\033[3mEnter your text below:\033[0m\n")

input_text = input()
            
# store the input text is a temp string where editted text is stored
temp_string = input_text

# create a list containing style choices
# [Bold, italic, underline, red, green, blue]
styles = ['B','i','u','r','g','b']

# loop through each style and check the input text for the symbol
for i, style in enumerate(styles):
    
    style_code = '<'+style+'>'
    
    # split the text by the style code
    editor = temp_string.split(style_code)
    
    # loop through each section in the editor list
    for j, text in enumerate(editor):
        
        # apply the style change to every odd index
        if j % 2 != 0:
            
            editor[j] = style_text(text,style_code)
            
    temp_string = "".join(editor)
    
output_text = temp_string

print("\n\033[4mOutput:\033[0m\n")
print(output_text)