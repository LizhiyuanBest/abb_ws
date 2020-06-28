; Auto-generated. Do not edit!


(cl:in-package abb_irb120-srv)


;//! \htmlinclude pos_speed-request.msg.html

(cl:defclass <pos_speed-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass pos_speed-request (<pos_speed-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pos_speed-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pos_speed-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name abb_irb120-srv:<pos_speed-request> is deprecated: use abb_irb120-srv:pos_speed-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pos_speed-request>) ostream)
  "Serializes a message object of type '<pos_speed-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pos_speed-request>) istream)
  "Deserializes a message object of type '<pos_speed-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pos_speed-request>)))
  "Returns string type for a service object of type '<pos_speed-request>"
  "abb_irb120/pos_speedRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pos_speed-request)))
  "Returns string type for a service object of type 'pos_speed-request"
  "abb_irb120/pos_speedRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pos_speed-request>)))
  "Returns md5sum for a message object of type '<pos_speed-request>"
  "556fae5da7a1874be33b0b17716aa737")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pos_speed-request)))
  "Returns md5sum for a message object of type 'pos_speed-request"
  "556fae5da7a1874be33b0b17716aa737")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pos_speed-request>)))
  "Returns full string definition for message of type '<pos_speed-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pos_speed-request)))
  "Returns full string definition for message of type 'pos_speed-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pos_speed-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pos_speed-request>))
  "Converts a ROS message object to a list"
  (cl:list 'pos_speed-request
))
;//! \htmlinclude pos_speed-response.msg.html

(cl:defclass <pos_speed-response> (roslisp-msg-protocol:ros-message)
  ((pos_x
    :reader pos_x
    :initarg :pos_x
    :type cl:fixnum
    :initform 0)
   (pos_y
    :reader pos_y
    :initarg :pos_y
    :type cl:fixnum
    :initform 0)
   (color
    :reader color
    :initarg :color
    :type cl:fixnum
    :initform 0)
   (speed
    :reader speed
    :initarg :speed
    :type cl:float
    :initform 0.0))
)

(cl:defclass pos_speed-response (<pos_speed-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pos_speed-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pos_speed-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name abb_irb120-srv:<pos_speed-response> is deprecated: use abb_irb120-srv:pos_speed-response instead.")))

(cl:ensure-generic-function 'pos_x-val :lambda-list '(m))
(cl:defmethod pos_x-val ((m <pos_speed-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader abb_irb120-srv:pos_x-val is deprecated.  Use abb_irb120-srv:pos_x instead.")
  (pos_x m))

(cl:ensure-generic-function 'pos_y-val :lambda-list '(m))
(cl:defmethod pos_y-val ((m <pos_speed-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader abb_irb120-srv:pos_y-val is deprecated.  Use abb_irb120-srv:pos_y instead.")
  (pos_y m))

(cl:ensure-generic-function 'color-val :lambda-list '(m))
(cl:defmethod color-val ((m <pos_speed-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader abb_irb120-srv:color-val is deprecated.  Use abb_irb120-srv:color instead.")
  (color m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <pos_speed-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader abb_irb120-srv:speed-val is deprecated.  Use abb_irb120-srv:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pos_speed-response>) ostream)
  "Serializes a message object of type '<pos_speed-response>"
  (cl:let* ((signed (cl:slot-value msg 'pos_x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'pos_y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'color)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pos_speed-response>) istream)
  "Deserializes a message object of type '<pos_speed-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'pos_x) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'pos_y) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'color) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'speed) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pos_speed-response>)))
  "Returns string type for a service object of type '<pos_speed-response>"
  "abb_irb120/pos_speedResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pos_speed-response)))
  "Returns string type for a service object of type 'pos_speed-response"
  "abb_irb120/pos_speedResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pos_speed-response>)))
  "Returns md5sum for a message object of type '<pos_speed-response>"
  "556fae5da7a1874be33b0b17716aa737")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pos_speed-response)))
  "Returns md5sum for a message object of type 'pos_speed-response"
  "556fae5da7a1874be33b0b17716aa737")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pos_speed-response>)))
  "Returns full string definition for message of type '<pos_speed-response>"
  (cl:format cl:nil "int16 pos_x~%int16 pos_y~%int16 color~%float32 speed~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pos_speed-response)))
  "Returns full string definition for message of type 'pos_speed-response"
  (cl:format cl:nil "int16 pos_x~%int16 pos_y~%int16 color~%float32 speed~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pos_speed-response>))
  (cl:+ 0
     2
     2
     2
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pos_speed-response>))
  "Converts a ROS message object to a list"
  (cl:list 'pos_speed-response
    (cl:cons ':pos_x (pos_x msg))
    (cl:cons ':pos_y (pos_y msg))
    (cl:cons ':color (color msg))
    (cl:cons ':speed (speed msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'pos_speed)))
  'pos_speed-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'pos_speed)))
  'pos_speed-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pos_speed)))
  "Returns string type for a service object of type '<pos_speed>"
  "abb_irb120/pos_speed")