# -- motrack.py User Configuration Settings -------

#======================================
# Logging Settings
#======================================
LOGGING_ON = True          # Show individual track xy points
SHOW_SETTINGS_ON = False   # Display settings on launch

#======================================
# Image Settings
# Camera Settings See configcam.py
#======================================
CAMERA = "pilibcam"   # valid values usbcam, rtspcam, pilibcam, pilegcam
USBCAM_SRC = 0
RTSPCAM_SRC = "rtsp://user:password@IP:554/path"

IM_SIZE = (640, 480)
IM_VFLIP = True
IM_HFLIP = True
IM_ROTATION = 0
IM_FRAMERATE = 30
IM_PREFIX = "track-"       # Prefix for image files
IM_DIR = "./media/images"  # directory for saving images (auto created)
IM_BIGGER = 1.75           # Resize the stream image before saving

#======================================
# Motion Tracking Settings
#======================================
TRACK_MIN_AREA = 500    # Minimum area of contours to track
TRACK_TRIG_AUTO = True  # True Auto Calculates TRIG_LEN and INTERVAL_LEN.
TRACK_TRIG_LEN = 150    # Number of pixels to end tracking
TRACK_INTERVAL_LEN = 50 # Max allowed px distance from previous
TRACK_TIMEOUT_SEC = 2.0 # If no motion for timeout seconds end tracking
TRACK_DELAY_SEC = 3.0   # seconds to delay after successful track.  Avoids duplicates
TRACK_HIST_ON = True    # Show track History overlayed on last image

#======================================
# Color data for OpenCV lines and text
#======================================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)

#======================================
# opencv settings. (Should Not need to be changed)
#======================================
GUI_ON = False      # Display image Stream on Desktop GUI
CIRCLE_ON = True
CIRCLE_SIZE = 5
LINE_COLOR = RED
LINE_THICKNESS = 2

TRACK_MIN_AREA = 500    # Minimum area of contours to track
THRESHOLD_SENSITIVITY = 25 # black pixels below value, white above to enhance contours
BLUR_SIZE = 10    # Enlarge white area around contour pixels to aid detection

#======================================
#       webserver.py Settings
#======================================

# Web Server settings
# -------------------
WEB_SERVER_PORT = 8090        # Default= 8090 Web server access port eg http://192.168.1.100:8080
WEB_SERVER_ROOT = "media"     # Default= "media" webserver root path to webserver image/video sub-folders
WEB_PAGE_TITLE = "MOTRACK2"   # web page title that browser show (not displayed on web page)
WEB_PAGE_REFRESH_ON = True    # False=Off (never)  Refresh True=On (per seconds below)
WEB_PAGE_REFRESH_SEC = "900"  # Default= "900" seconds to wait for web page refresh  seconds (15 minutes)
WEB_PAGE_BLANK_ON = False     # True Starts left image with a blank page until a right menu item is selected
                              # False displays second list[1] item since first may be in progress

# Left iFrame Image Settings
# --------------------------
WEB_IMAGE_HEIGHT = "768"       # Default= "768" px height of images to display in iframe
WEB_IFRAME_WIDTH_PERCENT = "70%" # Left Pane - Sets % of total screen width allowed for iframe. Rest for right list
WEB_IFRAME_WIDTH = "100%"      # Desired frame width to display images. can be eg percent "80%" or px "1280"
WEB_IFRAME_HEIGHT = "100%"     # Desired frame height to display images. Scroll bars if image larger (percent or px)

# Right Side Files List
# ---------------------
WEB_MAX_LIST_ENTRIES = 0           # 0 = All or Specify Max right side file entries to show (must be > 1)
WEB_LIST_HEIGHT = WEB_IMAGE_HEIGHT # Right List - side menu height in px (link selection)
WEB_LIST_BY_DATETIME_ON = True     # True=datetime False=filename
WEB_LIST_SORT_DESC_ON = True       # reverse sort order (filename or datetime per web_list_by_datetime setting

# ---------- End of User Variables ------------
