from instapy import InstaPy
from instapy import smart_run


session = InstaPy(username = "pomeranianroom", password = "pompom1022", headless_browser=False)

with smart_run(session):


    ##ここからは前設定

    #1_コメントを行う割合設定
    #session.set_do_comment(enabled=True, percentage=8)

    #2_コメントの内容設定(10種類)
    #session.set_comments([u'♡♡♡♡ @{}', u'Nice shot♡ @{}', u'💛💛💛 @{}', u'👏👏 @{}', u'👍👍 @{}', u'😍😍😍 @{}', u'😄😄😄 @{}', u'💘 @{}', u'Sweetie 😍♡ @{}', u'Cutie 😍 @{}'])

    #3_フォローを行う確率設定
    #session.set_do_follow(enabled=True, percentage=8, times=1)

    #4_各種アクションの1時間/1日当たり限度設定
    session.set_quota_supervisor(enabled=False, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=60, peak_likes_daily=100, peak_comments_hourly=None, peak_comments_daily=None,
                                peak_follows_hourly=None, peak_follows_daily=None, peak_unfollows_hourly=None, peak_unfollows_daily=None, peak_server_calls_hourly=2000, peak_server_calls_daily=4500)

    #5_いいね！を行わない制限設定
    #session.set_dont_like(['#exactmatch', '[startswith', ']endswith', 'broadmatch'])

    #6_#5で制限した内、特定のワードは無視する設定
    #session.set_ignore_if_contains(['glutenfree', 'french', 'tasty'])

    #7_あるユーザーの画像は完全に無視する設定
    #session.set_ignore_users(['random_user', 'another_username'])

    #8_あるワードが存在した場合はいいね！を行う設定
    #session.set_mandatory_words(['#pomeranian', '#pomstagram'])

    #9_説明欄の言語がある特定の言語以外ならアクションを制限する。
    #session.set_mandatory_language(enabled=True, character_set=['LATIN'])

    #10_アクティブユーザーはアンフォローしない設定
    #session.set_dont_unfollow_active_users(enabled=True, posts=15)

    #11_あるユーザーに対してアクションをスキップする設定
    #session.set_skip_users(skip_private=True, private_percentage=100, skip_no_profile_pic=False, no_profile_pic_percentage=100, skip_business=False, skip_non_business=False, business_percentage=100, skip_business_categories=[], dont_skip_business_categories=[], skip_bio_keyword=[], mandatory_bio_keywords=[])

    #12_あるユーザーの投稿画像が持ついいね！数によるアクションの制限設定
    #session.set_delimit_liking(enabled=True, max_likes=1005, min_likes=20)

    #13_あるユーザーの投稿画像が持つコメント数によるアクションの制限設定
    #session.set_delimit_commenting(enabled=True, max_comments=32, min_comments=0)
    
    #14_特定のワードが説明欄に含まれていたらコメントを行う設定
    #session.set_delimit_commenting(enabled=True, comments_mandatory_words=['cat', 'dog'])

    #15_ユーザーのフォロー数、フォロワー数によるアクションの制限設定
    session.set_relationship_bounds(enabled=False, delimit_by_numbers=True, max_followers=None, min_followers=None, max_following=None, min_following=None, potency_ratio=None, min_posts=None, max_posts=None)

    #16_ユーザーの投稿数によるアクションの制限設定
    #session.set_relationship_bounds(min_posts=10, max_posts=1000)

    #17_いいね！やフォローなどの詳細時間設定
    session.set_action_delays(enabled=True, like=3, comment=2, follow=2, unfollow=28, story=5, randomize=True, random_range_from=50, random_range_to=300, safety_match=True)


    ##ここまでが前設定



    ##ここからがアクション設定

    #1_いいね！を行うアクション
    #session.set_user_interact(amount=1, randomize=True, percentage=8, media='Photo')
    session.like_by_tags(tags=['ポメラニアン','pomeranian'], use_random_tags=True, amount=15, skip_top_posts=True, randomize=False, media=None, interact=True)
