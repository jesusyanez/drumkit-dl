

# urls
# [1] https://drive.google.com/drive/folders/1Iutl5GPdBU0Sps1zqY1HdYSw_0VWCZo2?usp=sharing  GDRIVEDL
# [2] https://drive.google.com/drive/folders/1XVpJyWDIUHbmjbMHrU0OsNXeYy_RsupM?usp=sharing
# [3] https://drive.google.com/drive/folders/1x0uGFhjYZqOYd-vEqwvVitRk5GCoAlzv?usp=sharing
# [4] https://drive.google.com/drive/folders/1VaXxeMyZbuN6Qf2L_tOkjdZVFt-uOPaZ?usp=sharing
# [5] https://drive.google.com/drive/folders/14PjpIRtPwvIInqngZoVJ1HTdMcHJfQNh?usp=sharing
# [6] https://drive.google.com/drive/folders/176dauAKpzN8Uo5KpGY84zQcLn7KKRy53?usp=sharing
# [7] https://drive.google.com/drive/folders/1MYJ_pQgaRX69Aw5ss1FqCni1Dw31a_S4?usp=sharing
# [8] https://drive.google.com/file/d/1HKfmfvm10RmaGUkJEvWJ6rgzr78ZbFOp/view?usp=sharing   ERROR
# [9] https://drive.google.com/drive/u/1/my-drive
# [10] https://drive.google.com/file/d/1ysrt8oN7AATFHLxG_iW2w3nqflXcaKr7/view?usp=sharing   ERROR
# [11] https://drive.google.com/drive/u/1/folders/1KJ51wdZfw_a5R3FTC1vIISKcsF_qZrJY
# [12] https://drive.google.com/drive/folders/1KJ51wdZfw_a5R3FTC1vIISKcsF_qZrJY?usp=sharing
# [13] https://drive.google.com/drive/folders/1YT-L8lR-FVs5AqcFUdXhAf5Htw7bVppx?usp=sharing
# [14] https://drive.google.com/drive/folders/1moxaIWrnYxSk4It-wH2uyk-ohLBqg8Eb?usp=sharing
# [15] https://drive.google.com/file/d/1Vn9uYvI49gp0XedJcNJBhIBInQbZsL5P/view?usp=sharing
# [16] https://drive.google.com/file/d/1beQtNpmOM7PoijbEZSz92SZPEOZ2hvPr/view
# [17] https://drive.google.com/file/d/1iBfCPFhymOzsmFQ9T-FoWkUHh7d0h0Qx/view?usp=sharing
# [18] https://drive.google.com/file/d/1_VcFfjJanL5aIvUsGlUnmEyD7CD2xhJi/view?usp=sharing
# [19] https://drive.google.com/file/d/1J9AVkTWm-lzJtq4Y9mOdVQAHcxjvDZaR/view?usp=sharing
# [20] https://drive.google.com/file/d/1ZapJwNkO7MFGDH1PB3i6AZ7KCRBl48r2/view?usp=drivesdk
# [21] https://drive.google.com/file/d/1g32OrfqrzCgebrwSBn1CaJF_-m9YEUSv/view?usp=sharing
# [22] https://drive.google.com/file/d/1nh8TE25SCY3fjZYZ7vQVYAnfRMzv9ZR_/view?usp=sharing

import gdown

# same as the above, and you can copy-and-paste a URL from Google Drive with fuzzy=True
# url = "https://drive.google.com/file/d/1HKfmfvm10RmaGUkJEvWJ6rgzr78ZbFOp/view?usp=sharing"
# output = "drumkit.zip"
# gdown.download(url=url, output=output, quiet=False, fuzzy=True)



import gdrivedl
import os

title = './drumkit'
url = 'https://drive.google.com/drive/folders/14PjpIRtPwvIInqngZoVJ1HTdMcHJfQNh?usp=sharing'
command = 'py gdrivedl.py ' + url + ' -P ' + title
# command = 'py gdrivedl.py ' + url
print(command)
os.system(command)

# os.system("py gdrivedl.py https://drive.google.com/drive/folders/1XVpJyWDIUHbmjbMHrU0OsNXeYy_RsupM?usp=sharing -P " + title)



