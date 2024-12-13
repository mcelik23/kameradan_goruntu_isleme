from app.config import load_config
from app.logger import setup_logger
from app.streamer import Streamer
from app.image_process import renk_algilama, kontur_ciz
import cv2

def main():
    logger = setup_logger()
    logger.info("Uygulama baslatildi")

    config = load_config('config/config.toml')
    logger.info("Konfigurasyon yuklendi")

    streamer = Streamer()
    logger.info("Kamera baglantisi baslatildi")

    try:
        while True:
            try:
                frame = streamer.read_frame()
            except Exception as e:
                logger.error(f"Goruntu alinirken hata: {e}")

                break
            try:
                red_mask, yellow_mask, green_mask = renk_algilama(frame, config)
            except Exception as e:
                logger.error(f"Renk algilama islemi sirasinda hata: {e}")
                break
            try:
                kontur_ciz(frame, red_mask, (0, 0, 255), "Kirmizi")
                kontur_ciz(frame, yellow_mask, (0, 255, 255), "Sari")
                kontur_ciz(frame, green_mask, (0, 255, 0), "Yesil")
            except Exception as e:
                logger.error(f"Kontur cizim islemi sirasinda hata: {e}")
                break
            cv2.imshow("Kamera Goruntusu", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                logger.info("Kullanici cikis yapti")
                break
    except Exception as e:
        logger.error(f"Genel hata: {e}")
    finally:
        streamer.release()
        cv2.destroyAllWindows()
        logger.info("Uygulama kapatildi")

if __name__ == "__main__":
    main()
