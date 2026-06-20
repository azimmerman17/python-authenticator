# html taken from  Postmark Template 
# https://postmarkapp.com/transactional-email-templates/welcome
from config import Config
from app.email.welcome_email.css import css

def welcome_email(data, app):
  email = f"""
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="x-apple-disable-message-reformatting" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta name="color-scheme" content="light dark" />
        <meta name="supported-color-schemes" content="light dark" />
        <title></title>
        <style>{css}</style>
      </head>
      <body>
        <table class="email-wrapper" width="100%" cellpadding="0" cellspacing="0" role="presentation">
          <tr>
            <td align="center">
              <table class="email-content" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                <tr>
                  <td class="email-masthead">
                    <a href="{app['login_url']}" class="f-fallback email-masthead_name">
                    {app['company']}
                  </a>
                  </td>
                </tr>
                <!-- Email Body -->
                <tr>
                  <td class="email-body" width="570" cellpadding="0" cellspacing="0">
                    <table class="email-body_inner" align="center" width="570" cellpadding="0" cellspacing="0" role="presentation">
                      <!-- Body content -->
                      <tr>
                        <td class="content-cell">
                          <div class="f-fallback">
                            <h1>Welcome, {data['first_name']}!</h1>
                            <p>Thanks for joining the {app['company']}. We’re thrilled to have you on board. You can verify your email and login through the button below:</p>
                            <!-- Action -->
                            <table class="body-action" align="center" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                              <tr>
                                <td align="center">
                                  <!-- Border based button
                                  https://litmus.com/blog/a-guide-to-bulletproof-buttons-in-email-design -->
                                  <table width="100%" border="0" cellspacing="0" cellpadding="0" role="presentation">
                                    <tr>
                                      <td align="center">
                                        <a href="{app['login_url']}" class="f-fallback button" target="_blank">Verify Email</a>
                                      </td>
                                    </tr>
                                  </table>
                                </td>
                              </tr>
                            </table>
                            <p>For reference, here's your login information:</p>
                            <table class="attributes" width="100%" cellpadding="0" cellspacing="0" role="presentation">
                              <tr>
                                <td class="attributes_content">
                                  <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
                                    <tr>
                                      <td class="attributes_item">
                                        <span class="f-fallback">
                  <strong>Email:</strong> {data['email']}
                </span>
                                      </td>
                                    </tr>
                                    <tr>
                                      <td class="attributes_item">
                                        <span class="f-fallback">
                  <strong>Username:</strong> {data['user_name']}
                </span>
                                      </td>
                                    </tr>
                                  </table>
                                </td>
                              </tr>
                            </table>
                            <p>If you have any issue, feel free to submit a issue using <a href={app['support_url']}">our support form</a> or <a href=mailto:{Config.MAIL_REPLY}>email our support team</a> with any issues.</p>
                            <p>Thanks,
                              <br>Andrew and the {app['company']} team</p>
                            <!-- Sub copy -->
                          </div>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <tr>
                  <td>
                    <table class="email-footer" align="center" width="570" cellpadding="0" cellspacing="0" role="presentation">
                      <tr>
                        <td class="content-cell" align="center">
                          <p class="f-fallback sub align-center">
                            [Company Name, LLC]
                            <br>1234 Street Rd.
                            <br>Suite 1234
                          </p>
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </body>
    </html>
  """

  return email