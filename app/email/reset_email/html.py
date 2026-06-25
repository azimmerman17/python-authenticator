# html taken from  Postmark Template 
# https://postmarkapp.com/transactional-email-templates/reset-password

from app.email.reset_email.css import css 

def reset_password_email(person, otp, os, browser, app):
  homepage = app['homepage']
  support_url = app['support_url']
  company = app['company']

  first_name = person['first_name']
  last_name = person['last_name']

  # header with css
  header = f"""
    <meta name='viewport' content='width=device-width, initial-scale=1.0' />
    <meta name='x-apple-disable-message-reformatting' />
    <meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
    <title></title>
    <style>{css}</style>
    <meta name='color-scheme' content='light dark' />
    <meta name='supported-color-schemes' content='light dark' />
  """

  # body
  bodyTEMP = f"""
  <span class='preheader'>Use this code to reset your password. The code is only valid for 30 minutes.</span>
  <hr/>
  <table class='email-wrapper' width='100%' cellpadding='0' cellspacing='0' role='presentation'>
    <tr>
      <td align='center'>
        <table class='email-content' width='100%' cellpadding='0' cellspacing='0' role='presentation'>
          <tr>
            <td class='email-masthead'>
            </td>
          </tr>
          <!-- Email Body -->
          <tr>
            <td class='email-body' width='570' cellpadding='0' cellspacing='0'>
              <table class='email-body_inner' align='center' width='570' cellpadding='0' cellspacing='0' role='presentation'>
                <!-- Body content -->
                <tr>
                  <td class='content-cell'>
                    <div class='f-fallback'>
                      <h1>Hi {first_name} {last_name},</h1>
                      <p>You recently requested to reset your password for your {company} account. Use the code below to reset your password. <strong>This one time password is only valid for the next 30 minutes.</strong></p>
                      <!-- Action -->
                      <table class='body-action' align='center' width='100%' cellpadding='0' cellspacing='0' role='presentation'>
                        <tr>
                          <td align='center'>
                            <!-- Border based button https://litmus.com/blog/a-guide-to-bulletproof-buttons-in-email-design -->
                            <table class="attributes" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                              <tr>
                                <td class="attributes_content">
                                  <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
                                    <tr>
                                      <td class="attributes_item">
                                        <span class="f-fallback">
                                          {otp}
                                        </span>
                                      </td>
                                    </tr>  
                                  </table>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </table>
                      <p>For security, this request was received from a {os} device using {browser}. If you did not request a password reset, please ignore this email or <a href='${support_url}'>contact support</a> if you have questions.</p>
                      <p>Thanks,
                        <br>The {company} team
                      </p>
                      <!-- Sub copy -->
                    </div>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td>
        <table class='email-footer' align='center' width='570' cellpadding='0' cellspacing='0' role='presentation'>
          <tr>
            <td class='content-cell' align='center'>
              <p class='f-fallback sub align-center'>
                <a href='{homepage}' class='f-fallback email-masthead_name'>{company}</a>
                <br><a href='{support_url}' class='f-fallback email-masthead_name'>Report an Issue</a>
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
  """

  # full html
  html = f"""
  <!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'>
  <html xmlns='http://www.w3.org/1999/xhtml'>
    <head>
      {header}
    </head>
    <body>
      {bodyTEMP}
    </body>
  </html>
  """

  return html
