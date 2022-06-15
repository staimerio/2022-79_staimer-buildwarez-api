# Retic
from retic import Router

# Controllers
import controllers.wordpress as wordpress

router = Router()

router.post("/wordpress/movies", wordpress.build_wp_movies)
