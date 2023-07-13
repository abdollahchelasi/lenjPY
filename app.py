import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
import hydralit_components as hc
from annotated_text import annotated_text


con = sqlite3.connect("sql/picscols.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS pics(id TEXT, img BLOB, note TEXT)")


#make it look nice from the start
st.set_page_config(layout='wide',page_title=" دکوراسیون لنج محمدⓂ ",page_icon="https://static2.khabarfoori.com/thumbnail/wzvbyUgbP4Ud/Z16wE4UvYwwq6tR2EOJTejVKGi50irI1BRxa7rEvYTnP-Bf9ahgZsp-WJuyTV3Z4V6BMQR8T-nfsv9pue1duJHSipVMRzPlM/%D9%84%D9%86%D8%AC.jpg",initial_sidebar_state='collapsed',)

# specify the primary menu definition




with open('c.css') as f:
    st.markdown(f'<style>{f.read()}</style>' ,unsafe_allow_html=True,)

col1,col2=st.columns(2)

st.title(" دکوراسیون لنج Ⓜ ")


menu_data = [

    
    {'id':'صفحه اصلی','icon': "🏚", 'label':"صفحه اصلی",},

    {"id": "ادمین", "icon": "🕵🏻‍♀️", "label": "ورود ادمین"},
    {'id':'تماس با من','icon':"📞",'label':"تماس با من"},
    {'id':'','icon': "📎",'label':"نمونه کارها", 'submenu':[{'id':'دکوراسیون لنج','icon': "fa fa-paperclip", 'label':"دکوراسیون لنج"},{'id':'نجاری لنج','icon': "🪜", 'label':"نجاری لنج"},{'id':'لایه کاری لنج','icon': "fa fa-database", 'label':"لایه کاری لنج"}]},
    {'id':'خدمات لنج','icon': "📋", 'label':"خدمات لنج"},
    
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    
    
#     home_name='Home',
#     login_name='Logout',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned

)



st.info(f"{menu_id}")












if menu_id == "ادمین":
    username = st.text_input(label="نام کاربری", placeholder="Username")
    password = st.text_input(label="پسورد", placeholder="password", type="password")
    b = st.button("ورود")

    if username == "m" and password == "m5858":
        st.success("خوش آمدی ادمین")
        menu_data = option_menu(options=["پست های شما"], menu_title="")

    elif username or password == "admin":
        st.error("لطفا درست وارد کنید")


if menu_data == "پست های شما":
    st.success(
        "توجه : لطفا با اضافه کردن محصول محصولات خود رو کامل پر کنید (عکس محصول , کد محصول , نام محصول) این ها نباید خالی باشد"
    )
    st.error(
        "هشدار : کد و نام محصولات شما نباید مثل محصولات دیگه ای که اضافه میکنید باشد. کد محصولات رو با اعداد انگلیسی و از شماره بالا به پایین شروع کنید . مانند : ( از 999 شروع کنید به پایین) "
    )

    if st.button("اضافه کردن محصول"):
        cur.execute("INSERT INTO pics(id, img, note) VALUES(?,?,?)", ("", "", ""))
        con.commit()

    st.write("---")

    for row in cur.execute("SELECT rowid, id, img, note FROM pics ORDER BY id"):
        with st.form(f"ID-{row[0]}", clear_on_submit=True):
            imgcol, notecol = st.columns([3, 2])
            id = notecol.text_input("کد محصول", row[1])
            note = notecol.text_area("نام محصول", row[3])
            if row[2]:
                img = row[2]
                imgcol.image(row[2])
            file = imgcol.file_uploader("تصاویر", ["png", "jpg", "gif", "jpeg", "bmp"])
            if file:
                img = file.read()
            if notecol.form_submit_button("ذخیره محصول"):
                cur.execute(
                    "UPDATE pics SET id=?, img=?, note=? WHERE id=?;",
                    (id, img, note, str(row[1])),
                )

                con.commit()
                st.experimental_rerun()

            if notecol.form_submit_button("حذف محصول"):
                cur.execute(f"""DELETE FROM pics WHERE rowid="{row[0]}";""")
                con.commit()
                st.experimental_rerun()





if menu_id == 'صفحه اصلی':
    
    st.snow()

    col1,col2 = st.columns(2)

    with col1:
        st.header("دکوراسیون محمد ربیعی")
        st.write("دکوراسیون لنج با کلی خدمات در جزیره قشم")
        
        annotated_text(
    "خدمات ",
    ("دکوراسیون", "لنج"),
    " و ",
    ("لایه کاری", "لنج"),
    " و ",
    ("نجاری", "لنج"),
    " با چند سال سابقه کار ",
    ("تو", "حوزه های مختلف"),
    "  ",
    ("کاری", "در"),
    " لنج ",
    "."
)
    with col2:
        st.image("https://static2.khabarfoori.com/thumbnail/wzvbyUgbP4Ud/Z16wE4UvYwwq6tR2EOJTejVKGi50irI1BRxa7rEvYTnP-Bf9ahgZsp-WJuyTV3Z4V6BMQR8T-nfsv9pue1duJHSipVMRzPlM/%D9%84%D9%86%D8%AC.jpg")


    for row in cur.execute('SELECT rowid, id, img, note FROM pics ORDER BY id'):
    # with st.form(f'ID-{row[0]}', clear_on_submit=True):
        st.write("---")
        imgcol, notecol = st.columns([3, 2])
    # id=notecol.text_input('id', row[1])
        id=notecol.text_input('کد محصول', row[1])
        note=notecol.text_area('اسم محصول', row[3])

        
        if row[2]:
            img=row[2]
            imgcol.image(row[2])
            # st.markdown(f"[باز کردن نمونه کار]()")


if menu_id == 'تماس با من':
    col1 , col2= st.columns(2)
    with col1:
        st.markdown("[محمد ربیعی : 09363635858](tel:09363635858)")

    with col2:

        st.markdown("[ارسال پیام](sms:09363635858)")



if menu_id == 'دکوراسیون لنج':
   
    
    col1,col2=st.columns((2))
    with col1:
        with st.expander(expanded=True,label="کد 10"):
            st.image('https://cdn.balad.ir/crowd-images/all/original/ce9108e0e35d46769334f2248c7510b0-ei_1651982402690.jpg?x-img=v1/crop,x_0,y_472,w_2160,h_1215/autorotate')
            st.text("طرح ستاره")

            st.markdown("[باز کردن نمونه کار](https://cdn.balad.ir/crowd-images/all/original/ce9108e0e35d46769334f2248c7510b0-ei_1651982402690.jpg?x-img=v1/crop,x_0,y_472,w_2160,h_1215/autorotate)")

    with col2:
        with st.expander(expanded=True,label="کد 20"):
            st.image('https://lenj.vercel.app/l1.jpg')
            st.text("نمای لمبه")
            st.markdown("[باز کردن نمونه کار](https://lenj.vercel.app/l1.jpg)")





if menu_id == 'نجاری لنج':
    st.text("به زودی نمونه کارای نجاری قرار میگیرد.")




if menu_id == 'لایه کاری لنج':
    st.text("به زودی نمونه های لایه کاری قرار میگیرد.")






if menu_id == 'خدمات لنج':
    st.caption("""
    خدمات لنج سازی یکی از بهترین خدمات در لنج خدمات کلی است که با نجاری و لایه کاری و دکوراسیون لنج لمبه کاری میباشد
    """)















st.divider()

st.markdown("[طراحی شده توسط عبدالله چلاسی](https://abdollahchelasi.ir)")


st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
