var breadcrumbs =
{
  navCourse : function( courseId )
  {
    params = "course_id=" + courseId;
    params += "&breadcrumbs_nav_item=" + breadcrumbs.rightMostNavItem;
    params += "&current_url=" + encodeURIComponent( location.href );
    params += "&parent_url=" + encodeURIComponent( breadcrumbs.rightMostParentURL );
    location.href = "/webapps/blackboard/execute/navCourse?" + params;
  }
};