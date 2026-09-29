def multi_stage_cipher(text):
    eng_to_ar = {
        'a': 'ش', 'b': 'لا', 'c': 'ؤ', 'd': 'ي', 'e': 'ث', 'f': 'ب', 'g': 'ل', 
        'h': 'ا', 'i': 'ه', 'j': 'ت', 'k': 'ن', 'l': 'م', 'm': 'ة', 'n': 'ى', 
        'o': 'خ', 'p': 'ح', 'q': 'ض', 'r': 'ق', 's': 'س', 't': 'ف', 'u': 'ع', 
        'v': 'ر', 'w': 'ص', 'x': 'ء', 'y': 'غ', 'z': 'ئ'
    }
    
    ar_rot13 = {
        'ا': 'ص', 'ب': 'ض', 'ت': 'ط', 'ث': 'ظ', 'ج': 'ع', 'ح': 'غ', 'خ': 'ف',
        'د': 'ق', 'ذ': 'ك', 'ر': 'ل', 'ز': 'م', 'س': 'ن', 'ش': 'ه', 'ص': 'و',
        'ض': 'ي', 'ط': 'ا', 'ظ': 'ب', 'ع': 'ت', 'غ': 'ث', 'ف': 'ج', 'ق': 'ح',
        'ك': 'خ', 'ل': 'د', 'م': 'ذ', 'ن': 'ر', 'ه': 'ز', 'و': 'س', 'ي': 'ش'
    }
    
    ar_to_eng_final = {
        'ص': 'w', 'ض': 'q', 'ط': "'", 'ظ': '/', 'ع': 'u', 'غ': 'y', 'ف': 't',
        'ق': 'r', 'ك': ';', 'ل': 'g', 'م': 'l', 'ن': 'k', 'ه': 'i', 'و': ',',
        'ي': 'd', 'ا': 'h', 'ب': 'f', 'ت': 'j', 'ث': 'e', 'ج': '[', 'ح': 'p',
        'خ': 'o', 'د': ']', 'ذ': '`', 'ر': 'v', 'ز': '.', 'س': 's', 'ش': 'a'
    }

    encrypted_text = ""

    for char in text.lower():
        if char == " ":
            encrypted_text += " "
            continue
            
        if char in eng_to_ar:
            arabic_char = eng_to_ar[char]
            
            if arabic_char in ar_rot13:
                shifted_arabic = ar_rot13[arabic_char]
                final_char = ar_to_eng_final[shifted_arabic]
                encrypted_text += final_char
            else:
                encrypted_text += "?"
        else:
            encrypted_text += char
            
    return encrypted_text


    

        
    

         
    












    
    




   
   
    





        



    
  




 

    
      





   

 

 
         
  

    