;; Auto-generated. Do not edit!


(when (boundp 'abb_irb120::pos_speed)
  (if (not (find-package "ABB_IRB120"))
    (make-package "ABB_IRB120"))
  (shadow 'pos_speed (find-package "ABB_IRB120")))
(unless (find-package "ABB_IRB120::POS_SPEED")
  (make-package "ABB_IRB120::POS_SPEED"))
(unless (find-package "ABB_IRB120::POS_SPEEDREQUEST")
  (make-package "ABB_IRB120::POS_SPEEDREQUEST"))
(unless (find-package "ABB_IRB120::POS_SPEEDRESPONSE")
  (make-package "ABB_IRB120::POS_SPEEDRESPONSE"))

(in-package "ROS")





(defclass abb_irb120::pos_speedRequest
  :super ros::object
  :slots ())

(defmethod abb_irb120::pos_speedRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass abb_irb120::pos_speedResponse
  :super ros::object
  :slots (_pos_x _pos_y _color _speed ))

(defmethod abb_irb120::pos_speedResponse
  (:init
   (&key
    ((:pos_x __pos_x) 0)
    ((:pos_y __pos_y) 0)
    ((:color __color) 0)
    ((:speed __speed) 0.0)
    )
   (send-super :init)
   (setq _pos_x (round __pos_x))
   (setq _pos_y (round __pos_y))
   (setq _color (round __color))
   (setq _speed (float __speed))
   self)
  (:pos_x
   (&optional __pos_x)
   (if __pos_x (setq _pos_x __pos_x)) _pos_x)
  (:pos_y
   (&optional __pos_y)
   (if __pos_y (setq _pos_y __pos_y)) _pos_y)
  (:color
   (&optional __color)
   (if __color (setq _color __color)) _color)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:serialization-length
   ()
   (+
    ;; int16 _pos_x
    2
    ;; int16 _pos_y
    2
    ;; int16 _color
    2
    ;; float32 _speed
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _pos_x
       (write-word _pos_x s)
     ;; int16 _pos_y
       (write-word _pos_y s)
     ;; int16 _color
       (write-word _color s)
     ;; float32 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _pos_x
     (setq _pos_x (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _pos_y
     (setq _pos_y (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _color
     (setq _color (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float32 _speed
     (setq _speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass abb_irb120::pos_speed
  :super ros::object
  :slots ())

(setf (get abb_irb120::pos_speed :md5sum-) "556fae5da7a1874be33b0b17716aa737")
(setf (get abb_irb120::pos_speed :datatype-) "abb_irb120/pos_speed")
(setf (get abb_irb120::pos_speed :request) abb_irb120::pos_speedRequest)
(setf (get abb_irb120::pos_speed :response) abb_irb120::pos_speedResponse)

(defmethod abb_irb120::pos_speedRequest
  (:response () (instance abb_irb120::pos_speedResponse :init)))

(setf (get abb_irb120::pos_speedRequest :md5sum-) "556fae5da7a1874be33b0b17716aa737")
(setf (get abb_irb120::pos_speedRequest :datatype-) "abb_irb120/pos_speedRequest")
(setf (get abb_irb120::pos_speedRequest :definition-)
      "
---
int16 pos_x
int16 pos_y
int16 color
float32 speed

")

(setf (get abb_irb120::pos_speedResponse :md5sum-) "556fae5da7a1874be33b0b17716aa737")
(setf (get abb_irb120::pos_speedResponse :datatype-) "abb_irb120/pos_speedResponse")
(setf (get abb_irb120::pos_speedResponse :definition-)
      "
---
int16 pos_x
int16 pos_y
int16 color
float32 speed

")



(provide :abb_irb120/pos_speed "556fae5da7a1874be33b0b17716aa737")


