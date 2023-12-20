import subprocess

from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas


def envelope(item_list, person_name=""):
    file_name = str(item_list[0])
    if person_name != "":
        file_name += "_notsend"
    canvas = Canvas(f"temp/{file_name}.pdf", pagesize=(9.5 * inch, 4.125 * inch))
    pdfmetrics.registerFont(TTFont('TH SarabunIT๙', 'resource/THSarabunIT๙.ttf'))
    canvas.setFont("TH SarabunIT๙", 16)
    canvas.drawString(2.5 * cm, 8 * cm, "พิสูจน์หลักฐานจังหวัดภูเก็ต")
    canvas.drawString(2.5 * cm, 7.4 * cm, "323/39 ถนนเยาวราช")
    canvas.drawString(2.5 * cm, 6.8 * cm, "ตำบลตลาดใหญ่ อำเภอเมืองภูเก็ต")
    canvas.drawString(2.5 * cm, 6.2 * cm, "จังหวัดภูเก็ต 83000")

    if person_name == "":
        canvas.drawString(6.5 * cm, 4.4 * cm, 'เรียน')
        canvas.drawString(7.5 * cm, 4.4 * cm, item_list[2])
        canvas.drawString(7.5 * cm, 3.8 * cm, item_list[3])
        canvas.drawString(7.5 * cm, 3.2 * cm, item_list[4])
        canvas.drawString(7.5 * cm, 2.6 * cm, item_list[5])
        canvas.drawString(7.5 * cm, 2 * cm, item_list[6])
        canvas.rect(16.5 * cm, 6 * cm, 5 * cm, 3 * cm)
        canvas.drawString(17 * cm, 8.25 * cm, 'ชำระค่าฝากส่งเป็นรายเดือน')
        canvas.drawString(17.5 * cm, 7.25 * cm, 'ใบอนุญาตที่ 61/2537')
        canvas.drawString(18.5 * cm, 6.25 * cm, 'ปท.ภูเก็ต')
    else:
        canvas.setFont("TH SarabunIT๙", 24)
        canvas.drawString(6.5 * cm, 4.4 * cm, 'เรียน')
        canvas.drawString(8 * cm, 4.4 * cm, item_list[1])
        if person_name != "()":
            canvas.drawString(8 * cm, 3.4 * cm, person_name)
    try:
        canvas.save()
    except PermissionError:
        print('p error')
    else:
        subprocess.run(['start', '', f"temp/{file_name}.pdf"], shell=True, check=True)


def a4(item_list, person_name=""):
    file_name = str(item_list[0]) + '_a4'
    if person_name != "":
        file_name += "_notsend"
    canvas = Canvas(f"temp/{file_name}.pdf", pagesize=(29.7 * cm, 21 * cm))
    canvas.rect(1 * cm, 1 * cm, 27.7 * cm, 19 * cm)
    canvas.drawImage(f"resource/garuda.jpg", 2 * cm, 16 * cm, width=3 * cm, height=3 * cm)
    pdfmetrics.registerFont(TTFont('TH SarabunIT๙', 'resource/THSarabunIT๙ Bold.ttf'))
    canvas.setFont("TH SarabunIT๙", 24)
    canvas.drawString(2 * cm, 15 * cm, "พิสูจน์หลักฐานจังหวัดภูเก็ต")
    canvas.drawString(2 * cm, 14 * cm, "323/39 ถนนเยาวราช")
    canvas.drawString(2 * cm, 13 * cm, "ตำบลตลาดใหญ่ อำเภอเมืองภูเก็ต")
    canvas.drawString(2 * cm, 12 * cm, "จังหวัดภูเก็ต 83000")
    canvas.drawString(8 * cm, 10 * cm, 'เรียน')
    if person_name == "":
        canvas.drawString(9.5 * cm, 10 * cm, item_list[2])
        canvas.drawString(9.5 * cm, 9 * cm, item_list[3])
        canvas.drawString(9.5 * cm, 8 * cm, item_list[4])
        canvas.drawString(9.5 * cm, 7 * cm, item_list[5])
        canvas.drawString(9.5 * cm, 6 * cm, item_list[6])
        canvas.rect(19.2 * cm, 15 * cm, 8.5 * cm, 4 * cm)
        canvas.drawString(20.2 * cm, 18 * cm, 'ชำระค่าฝากส่งเป็นรายเดือน')
        canvas.drawString(20.6 * cm, 17 * cm, 'ใบอนุญาตที่ 61/2537')
        canvas.drawString(22.2 * cm, 16 * cm, 'ปท.ภูเก็ต')
    else:
        canvas.drawString(9.5 * cm, 10 * cm, item_list[1])
        if person_name != "()":
            each_person = person_name.split(', ')
            for count, name in enumerate(each_person):
                canvas.drawString(11.5 * cm, (9-count) * cm, name)
    try:
        canvas.save()
    except PermissionError:
        print('p error')
    else:
        subprocess.run(['start', '', f"temp/{file_name}.pdf"], shell=True, check=True)


if __name__ == "__main__":
    # envelope(12)
    pass
