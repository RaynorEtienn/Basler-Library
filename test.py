from pypylon import pylon
import cv2

def open_basler_image():
    # Connect to the first available Basler camera
    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

    try:
        # Open the camera
        camera.Open()

        # Set the camera parameters
        camera.PixelFormat = "Mono8"

        # Grab a single image using GrabOne
        grab_result = camera.GrabOne(5000)
        
        if grab_result.GrabSucceeded():
            # Get the image data as a numpy array
            image_data = grab_result.Array

            # Display the RGB image
            cv2.imshow("Basler Image", image_data)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    except Exception as e:
        print("Error: " + str(e))

    # Close the camera
    camera.Close()

open_basler_image()