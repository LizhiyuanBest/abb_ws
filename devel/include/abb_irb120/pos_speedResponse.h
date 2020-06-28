// Generated by gencpp from file abb_irb120/pos_speedResponse.msg
// DO NOT EDIT!


#ifndef ABB_IRB120_MESSAGE_POS_SPEEDRESPONSE_H
#define ABB_IRB120_MESSAGE_POS_SPEEDRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace abb_irb120
{
template <class ContainerAllocator>
struct pos_speedResponse_
{
  typedef pos_speedResponse_<ContainerAllocator> Type;

  pos_speedResponse_()
    : pos_x(0)
    , pos_y(0)
    , color(0)
    , speed(0.0)  {
    }
  pos_speedResponse_(const ContainerAllocator& _alloc)
    : pos_x(0)
    , pos_y(0)
    , color(0)
    , speed(0.0)  {
  (void)_alloc;
    }



   typedef int16_t _pos_x_type;
  _pos_x_type pos_x;

   typedef int16_t _pos_y_type;
  _pos_y_type pos_y;

   typedef int16_t _color_type;
  _color_type color;

   typedef float _speed_type;
  _speed_type speed;





  typedef boost::shared_ptr< ::abb_irb120::pos_speedResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::abb_irb120::pos_speedResponse_<ContainerAllocator> const> ConstPtr;

}; // struct pos_speedResponse_

typedef ::abb_irb120::pos_speedResponse_<std::allocator<void> > pos_speedResponse;

typedef boost::shared_ptr< ::abb_irb120::pos_speedResponse > pos_speedResponsePtr;
typedef boost::shared_ptr< ::abb_irb120::pos_speedResponse const> pos_speedResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::abb_irb120::pos_speedResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::abb_irb120::pos_speedResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace abb_irb120

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::abb_irb120::pos_speedResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::abb_irb120::pos_speedResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::abb_irb120::pos_speedResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::abb_irb120::pos_speedResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::abb_irb120::pos_speedResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::abb_irb120::pos_speedResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::abb_irb120::pos_speedResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "556fae5da7a1874be33b0b17716aa737";
  }

  static const char* value(const ::abb_irb120::pos_speedResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x556fae5da7a1874bULL;
  static const uint64_t static_value2 = 0xe33b0b17716aa737ULL;
};

template<class ContainerAllocator>
struct DataType< ::abb_irb120::pos_speedResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "abb_irb120/pos_speedResponse";
  }

  static const char* value(const ::abb_irb120::pos_speedResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::abb_irb120::pos_speedResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 pos_x\n\
int16 pos_y\n\
int16 color\n\
float32 speed\n\
\n\
";
  }

  static const char* value(const ::abb_irb120::pos_speedResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::abb_irb120::pos_speedResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.pos_x);
      stream.next(m.pos_y);
      stream.next(m.color);
      stream.next(m.speed);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct pos_speedResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::abb_irb120::pos_speedResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::abb_irb120::pos_speedResponse_<ContainerAllocator>& v)
  {
    s << indent << "pos_x: ";
    Printer<int16_t>::stream(s, indent + "  ", v.pos_x);
    s << indent << "pos_y: ";
    Printer<int16_t>::stream(s, indent + "  ", v.pos_y);
    s << indent << "color: ";
    Printer<int16_t>::stream(s, indent + "  ", v.color);
    s << indent << "speed: ";
    Printer<float>::stream(s, indent + "  ", v.speed);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ABB_IRB120_MESSAGE_POS_SPEEDRESPONSE_H
