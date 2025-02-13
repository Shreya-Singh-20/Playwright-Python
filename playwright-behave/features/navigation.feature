Feature: Navigation from Header

  @navigation
  Scenario Outline: User navigates to different sections from the header
    Given I open the Amazon website
    When I click on "<menu_option>" from the header
    Then I should be navigated to the "<expected_page>"

  Examples:
    | menu_option      | expected_page                                                                                       |
    | All              | https://www.amazon.in/     |
    | Fresh            | https://www.amazon.in/alm/storefront?almBrandId=ctnow&ref_=nav_cs_fresh                             |
    | MX Player        | https://www.amazon.in/minitv?ref_=nav_avod_desktop_topnav                                           |
    | Sell             | https://www.amazon.in/b/32702023031?node=32702023031&ld=AZINSOANavDesktop_T3&ref_=nav_cs_sell_T3    |
    | Best Sellers     | https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers                                       |
    | Mobiles          | https://www.amazon.in/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles                  |
    | Today's Deals    | https://www.amazon.in/deals?ref_=nav_cs_gb                                                          |
    | Customer Service | https://www.amazon.in/gp/help/customer/display.html?nodeId=200507590&ref_=nav_cs_help               |
    | Electronics      | https://www.amazon.in/electronics/b/?ie=UTF8&node=976419031&ref_=nav_cs_electronics                 |
    | Amazon Pay       | https://www.amazon.in/amazonpay/home?ref_=nav_cs_apay                                               |
    | Prime            | https://www.amazon.in/amazonprime?ref_=nav_cs_primelink_nonmember                                   |
    | New Releases     | https://www.amazon.in/gp/new-releases/?ref_=nav_cs_newreleases                                      |
    | Home & Kitchen   | https://www.amazon.in/Home-Kitchen/b/?ie=UTF8&node=976442031&ref_=nav_cs_home                       |