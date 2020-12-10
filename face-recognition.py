from PIL import Image, ImageDraw
import face_recognition

def face_recognition_list(filename):
    test_image = face_recognition.load_image_file(filename)

    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)  
        name = "Unknown Person"  
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

image_of_monica = face_recognition.load_image_file('./known/Monica Gellar.png')
monica_face_encoding = face_recognition.face_encodings(image_of_monica)[0]

image_of_ross = face_recognition.load_image_file('./known/Ross Gellar.jpg')
ross_face_encoding = face_recognition.face_encodings(image_of_ross)[0]

image_of_chandler = face_recognition.load_image_file('./known/Chandler Bing.jpg')
chandler_face_encoding = face_recognition.face_encodings(image_of_chandler)[0]

image_of_joey = face_recognition.load_image_file('./known/Joey Tribbiani.jpg')
joey_face_encoding = face_recognition.face_encodings(image_of_joey)[0]

image_of_rachel = face_recognition.load_image_file('./known/Rachel Green.jpg')
rachel_face_encoding = face_recognition.face_encodings(image_of_rachel)[0]

image_of_phoebe = face_recognition.load_image_file('./known/Phoebe Buffay.jpg')
phoebe_face_encoding = face_recognition.face_encodings(image_of_phoebe)[0]


known_face_encodings = [
    monica_face_encoding,
    ross_face_encoding,
    joey_face_encoding,
    phoebe_face_encoding,
    rachel_face_encoding,
    chandler_face_encoding
]

known_face_names = [
    "Monica Gellar",
    "Ross Gellar",
    "Joey Tribbiani",
    "Phoebe Buffay",
    "Rachel Green",
    "Chandler Bing"
]

test_image = face_recognition.load_image_file('./group/group_1.jpg')

face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)

draw = ImageDraw.Draw(pil_image)

print(f'There are {len(face_locations)} people in the image.')

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)  
    name = "Unknown Person"  

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    
    draw.rectangle(((left, top),(right, bottom)), outline = (0,0,00))

    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height), (right, bottom)), fill = (0,0,0), outline = (0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill = (255,255,255,255))

del draw

pil_image.show()