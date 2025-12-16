import streamlit as st
import qrcode
from io import BytesIO
import uuid
from PIL import Image
from gtts import gTTS
import base64

def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img
st.title("metro ticket booking system with QR Code + Auto Voice")
stations = ["ameerpet","miyapur","lb nagar","kphb","jntu"]
name=st.text_input("passenger name")
source=st.selectbox("source station",stations)
destination=st.selectbox("destination station",stations)
no_tickets=st.number_input("number of tickets",min_value=1, value=1)
price_per_ticket=30
total_amount=no_tickets+price_per_ticket
st.info(f"total amount:{total_amount}")
if st.button("book ticket"):
    if name.strip()=="":
        st.error("please enter passenger name")
    elif source==destination:
        st.error("source and destination cannot be the same")
    else:
        booking_id=str(uuid.uuid4())[:8]

#qr code generator
        qr_data=(
         f"BookingID:{booking_id}\n"
         f"Name:{name}\nFrom:{source}\nDestination:{destination}\n Tickets:{no_tickets}")
        qr_img=generate_qr(qr_data)
        buf=BytesIO()
        qr_img.save(buf, format="PNG")
        qr_bytes=buf.getvalue()

        st.success("Ticket Booked Successfully")

        st.write("Ticket Details")
        st.write(f"Booking ID:{booking_id}")
        st.write(f"Passenger:{name}")
        st.write(f"From:{source}")
        st.write(f"To:{destination}")
        st.write(f"Tickets:{no_tickets}")
        st.write(f"Amount Paid:{total_amount}")
        st.image(qr_bytes,width=250)
        
