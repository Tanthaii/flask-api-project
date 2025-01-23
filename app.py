from flask import Flask, request, jsonify

app = Flask(__name__)

# ตัวอย่างข้อมูลโรคของน้องหมาและน้องแมว
diseases = [
    {
        "id": 1,
        "name": "พยาธิหนอนหัวใจ",
        "species": "สุนัข",
        "symptoms": ["ไอเรื้อรัง", "อ่อนเพลีย", "หายใจลำบาก"],
        "prevention": "ให้ยาป้องกันพยาธิหนอนหัวใจอย่างสม่ำเสมอ",
        "treatment": "ใช้ยาเพื่อกำจัดพยาธิตามคำแนะนำของสัตวแพทย์"
    },
    {
        "id": 2,
        "name": "ไข้หัดแมว",
        "species": "แมว",
        "symptoms": ["ไข้สูง", "อาเจียน", "ท้องเสีย", "เบื่ออาหาร"],
        "prevention": "ฉีดวัคซีนป้องกันไข้หัดแมว",
        "treatment": "รักษาตามอาการและให้ของเหลวทดแทน" 
    }
]

# Endpoint: ดึงข้อมูลโรคทั้งหมด
@app.route('/diseases', methods=['GET'])
def get_diseases():
    return jsonify(diseases)

# Endpoint: ดึงข้อมูลโรคเฉพาะตาม ID
@app.route('/diseases/<int:disease_id>', methods=['GET'])
def get_disease_by_id(disease_id):
    disease = next((d for d in diseases if d["id"] == disease_id), None)
    if disease:
        return jsonify(disease)
    else:
        return jsonify({"error": "ไม่พบข้อมูลโรค"}), 404

# Endpoint: เพิ่มข้อมูลโรคใหม่
@app.route('/diseases', methods=['POST'])
def add_disease():
    new_disease = request.json
    new_disease["id"] = max(d["id"] for d in diseases) + 1 if diseases else 1
    diseases.append(new_disease)
    return jsonify(new_disease), 201

# Endpoint: แก้ไขข้อมูลโรค
@app.route('/diseases/<int:disease_id>', methods=['PUT'])
def update_disease(disease_id):
    disease = next((d for d in diseases if d["id"] == disease_id), None)
    if disease:
        updates = request.json
        disease.update(updates)
        return jsonify(disease)
    else:
        return jsonify({"error": "ไม่พบข้อมูลโรค"}), 404

# Endpoint: ลบข้อมูลโรค
@app.route('/diseases/<int:disease_id>', methods=['DELETE'])
def delete_disease(disease_id):
    global diseases
    diseases = [d for d in diseases if d["id"] != disease_id]
    return jsonify({"message": "ลบข้อมูลสำเร็จ"})

if __name__ == '__main__':
    app.run(debug=True)

