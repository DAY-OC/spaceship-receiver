import cv2
import matplotlib.pyplot as plt
import time

# Create a list to store the pixel counts
pixel_counts = []

# Start webcam
cap = cv2.VideoCapture(0)

# Create a figure and axis for plotting
fig, ax = plt.subplots()

i=0

while True:
    # Get webcam frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # count the number of white pixels
    white_pixels = cv2.countNonZero(thresh)
    # if(white_pixels > 8000):
    #     white_pixels = 1
    # else:
    #     white_pixels = 0
    # add the count to the list
    pixel_counts.append(white_pixels)

    # Take the average
    average = sum(pixel_counts) / len(pixel_counts)

    # Plot the pixel count over time
    ax.clear()
    ax.plot(pixel_counts)
    print(i)

    print(average)
    
    i=i+1
    # add the count to the frame

    # Display thresholded frame
    cv2.imshow("Webcam", thresh)
    plt.pause(0.05)
    # sleep for 500 millisconds
    # time.sleep(0.2)

    # Exit program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close display window
cap.release()
cv2.destroyAllWindows()