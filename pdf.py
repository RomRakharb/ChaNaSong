from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import subprocess


def envelope(item_list, person_name=""):
    canvas = Canvas(f"temp/{str(item_list[0])}.pdf", pagesize=(9.5 * inch, 4.125 * inch))
    pdfmetrics.registerFont(TTFont('THSarabunNew', 'resource/THSarabunNew.ttf'))
    canvas.setFont("THSarabunNew", 16)
    canvas.drawString(3 * cm, 8 * cm, "พิสูจน์หลักฐานจังหวัดภูเก็ต")
    canvas.drawString(3 * cm, 7.4 * cm, "323/39 ถนนเยาวราช")
    canvas.drawString(3 * cm, 6.8 * cm, "ตำบลตลาดใหญ่ อำเภอเมืองภูเก็ต")
    canvas.drawString(3 * cm, 6.2 * cm, "จังหวัดภูเก็ต 83000")

    canvas.drawString(7 * cm, 5 * cm, 'เรียน')
    canvas.drawString(8 * cm, 5 * cm, item_list[2])
    canvas.drawString(8 * cm, 4.4 * cm, item_list[3])
    canvas.drawString(8 * cm, 3.8 * cm, item_list[4])
    canvas.drawString(8 * cm, 3.2 * cm, item_list[5])
    canvas.drawString(8 * cm, 2.6 * cm, item_list[6])

    canvas.rect(17 * cm, 6 * cm, 5 * cm, 3 * cm)
    canvas.drawString(17.5 * cm, 8.25 * cm, 'ชำระค่าฝากส่งเป็นรายเดือน')
    canvas.drawString(18 * cm, 7.25 * cm, 'ใบอนุญาตที่ 61/2537')
    canvas.drawString(19 * cm, 6.25 * cm, 'ปท.ภูเก็ต')

    try:
        canvas.save()
    except PermissionError:
        print('p error')
    else:
        subprocess.run(['start', '', f"temp/{str(item_list[0])}.pdf"], shell=True, check=True)


def a4(item_id):
    canvas = Canvas(f"temp/{item_id}.pdf", pagesize=(297 * cm, 210 * cm))
    canvas.drawString(10 * cm, 10 * cm, str(item_id))
    try:
        canvas.save()
    except PermissionError:
        print('p error')
    else:
        subprocess.run(['start', '', f"temp/{item_id}.pdf"], shell=True, check=True)


if __name__ == "__main__":
    # envelope(12)
    pass