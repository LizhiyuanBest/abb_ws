
(cl:in-package :asdf)

(defsystem "abb_irb120-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "pos_speed" :depends-on ("_package_pos_speed"))
    (:file "_package_pos_speed" :depends-on ("_package"))
  ))