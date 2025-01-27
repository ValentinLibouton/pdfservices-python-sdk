from src.ocrpdf.ocr_pdf import OcrPDF
import os
import json

def load_credentials_from_json(file_path):
    """Charge les identifiants client, secret et organisation depuis un fichier JSON."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier JSON spécifié n'existe pas : {file_path}")

    with open(file_path, "r") as json_file:
        credentials = json.load(json_file)

    # Vérification des clés dans le fichier JSON
    if "client_credentials" not in credentials or "service_principal_credentials" not in credentials:
        raise KeyError(
            "Le fichier JSON doit contenir les sections 'client_credentials' et 'service_principal_credentials'.")

    client_id = credentials["client_credentials"].get("client_id")
    client_secret = credentials["client_credentials"].get("client_secret")
    organization_id = credentials["service_principal_credentials"].get("organization_id")

    if not client_id or not client_secret or not organization_id:
        raise KeyError("Le fichier JSON doit inclure 'client_id', 'client_secret' et 'organization_id'.")

    return client_id, client_secret, organization_id

client_id, client_secret, _ = load_credentials_from_json("pdfservices-api-credentials.json")
filepath = input("Entrez le chemin du fichier: ")

op = OcrPDF(filepath=filepath, client_id=client_id, client_secret=client_secret)
link = op.create_output_file_path()
print(f"Le fichier se trouve: {link}")