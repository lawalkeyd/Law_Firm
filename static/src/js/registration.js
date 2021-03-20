// form visible
$('#law_personal_info_btn').on('click', function(){
    $('.law_personal_info').hide();
    $('.law_login_form').show();
  });
  
  // Presonal Information
  $('#law_login_btn').on('click', function(){
    $('.law_login_form').hide();
    $('.law_edu_form').show();
  });
  
  $('#law_login_prev_btn').on('click', function(){
    $('.law_login_form').hide();
    $('.law_personal_info').show();
  });
  
  // Education Information
  $('#law_edu_btn').on('click', function(){
    $('.law_edu_form').hide();
    $('.law_job_form').show();
  });
  
  $('#law_edu_prev_btn').on('click', function(){
    $('.law_edu_form').hide();
    $('.law_login_form').show();
  });
  
  // Job Information
  $('#law_job_btn').on('click', function(){
    $('.law_job_form').hide();
    $('.law_experience_form').show();
  });
  
  $('#law_job_prev_btn').on('click', function(){
    $('.law_job_form').hide();
    $('.law_edu_form').show();
  });
  
  
  // Previous Academic Certificate Information
  $('#law_exp_prev_btn').on('click', function(){
    $('.law_experience_form').hide();
    $('.law_job_form').show();
  });
  