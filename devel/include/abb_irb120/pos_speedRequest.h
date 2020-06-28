// Generated by gencpp from file abb_irb120/pos_speedRequest.msg
// DO NOT EDIT!


#ifndef ABB_IRB120_MESSAGE_POS_SPEEDREQUEST_H
#define ABB_IRB120_MESSAGE_POS_SPEEDREQUEST_H


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
struct pos_speedRequest_
{
  typedef pos_speedRequest_<ContainerAllocator> Type;

  pos_speedRequest_()
    {
    }
  pos_speedRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::abb_irb120::pos_speedRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::abb_irb120::pos_speedRequest_<ContainerAllocator> const> ConstPtr;

}; // struct pos_speedRequest_

typedef ::abb_irb120::pos_speedRequest_<std::allocator<void> > pos_speedRequest;

typedef boost::shared_ptr< ::abb_irb120::pos_speedRequest > pos_speedRequestPtr;
typedef boost::shared_ptr< ::abb_irb120::pos_speedRequest const> pos_speedRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::abb_irb120::pos_speedRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::abb_irb120::pos_speedRequest_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::abb_irb120::pos_speedRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::abb_irb120::pos_speedRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::abb_irb120::pos_speedRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::abb_irb120::pos_speedRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::abb_irb120::pos_speedRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::abb_irb120::pos_speedRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::abb_irb120::pos_speedRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::abb_irb120::pos_speedRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::abb_irb120::pos_speedRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "abb_irb120/pos_speedRequest";
  }

  static const char* value(const ::abb_irb120::pos_speedRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::abb_irb120::pos_speedRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
";
  }

  static const char* value(const ::abb_irb120::pos_speedRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::abb_irb120::pos_speedRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct pos_speedRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::abb_irb120::pos_speedRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::abb_irb120::pos_speedRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // ABB_IRB120_MESSAGE_POS_SPEEDREQUEST_H
