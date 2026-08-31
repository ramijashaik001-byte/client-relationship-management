# app/utils/pdf.py
import os
import logging
from typing import Dict, Any

logger = logging.getLogger("PDFUtility")

class OnboardingPDFGenerator:
    @staticmethod
    def generate_client_dossier(client_id: int, data: Dict[str, Any]) -> str:
        """
        Generates and formats an onboarding report document in PDF format.
        Stores generated artifact on disk.
        """
        logger.info(f"Generating client onboarding pdf dossier for client ID: {client_id}")
        os.makedirs("./storage/documents", exist_ok=True)
        file_path = f"./storage/documents/client_{client_id}_dossier.pdf"
        
        # Simple simulated writing of raw PDF structure tags
        with open(file_path, "w") as f:
            f.write(f"%PDF-1.4\n")
            f.write(f"% Client Dossier Report\n")
            f.write(f"Client ID: {client_id}\n")
            for k, v in data.items():
                f.write(f"{k}: {v}\n")
            f.write(f"%%EOF")
            
        logger.info(f"Dossier PDF saved to: {file_path}")
        return file_path

# PDF dossier rendering properties

    @staticmethod
    def get_default_pdf_theme() -> str:
        """Returns the branding theme style sheet name."""
        return "CRM_ENTERPRISE_LIGHT"
