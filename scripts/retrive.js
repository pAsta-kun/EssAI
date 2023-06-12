// Example Reddit links
const redditLinks = [
    'https://www.reddit.com/r/ApplyingToCollege/comments/ppetbb/hi_seniors_you_do_have_an_amazing_essay_inside/?context=3',
    'https://www.reddit.com/r/ApplyingToCollege/comments/pv8w4u/making_your_peace_with_the_supplemental_essays/?context=3',
    'https://www.reddit.com/r/ApplyingToCollege/comments/ee95h4/hello_beautiful_seniors_its_go_time_some_handy/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/ee94l2/admissionsmoms_last_minute_guide_to_super_quick/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/cybr0s/essay_thoughts_while_in_essay_review_mode_just/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/co4e33/hey_admissionmom_real_talk_from_reddit_free/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/o0jtz8/dont_put_your_admissions_readers_to_sleep_5_tips/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/pc03za/13_reasons_why_its_ok_to_write_about_trauma_in/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/p4giuz/a_sage_insight_about_the_college_essay_from_my/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/nvk8vq/a_simple_piece_of_writing_jiujitsu_to_make_your/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/p9d75z/the_scum_polisher_method_my_system_for_getting/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/o3n15t/dont_be_a_hammer_or_an_inert_blob_of_goo_how_to/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/yirjeo/8_of_the_biggest_common_app_mistakes_ive_seen_in/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/xx6c6t/heres_where_you_should_be_now_with_your/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/xf4on4/how_you_should_and_shouldnt_be_using_the/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/wrq2j5/one_of_your_essays_needs_to_communicate_a_case/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/vz09mf/the_document_in_every_application_most_students/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/baotoj/the_scholargrade_essay_series_part_1_how_to_start/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/bdyf1d/the_scholargrade_essay_series_part_2_throw_away/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/bgvslr/the_scholargrade_essay_series_part_3_conquering/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/bkg10a/the_scholargrade_essay_series_part_4_what_makes/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/9dp4u7/what_to_do_when_youre_over_the_word_count/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/aefjas/what_to_do_when_your_essay_is_too_short/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/8upen2/how_to_end_an_essay_gracefully/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/a9vfov/if_youre_wondering_what_an_acceptance_letter/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/9zg9sc/if_you_dont_have_a_first_draft_yet_dont_read_this/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/g9ps6z/how_to_choose_an_essay_topic/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/dfawfe/a_short_guide_to_short_essays/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/i5uure/how_to_fix_your_bad_essay/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/i6kn6o/it_all_started_with_essay_topics_heres_how_to/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/dti2r7/what_ive_learned_from_reading_tons_of_your_essays/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/du0axm/what_ive_learned_from_reading_tons_of_your_essays/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/heic2o/how_to_approach_the_common_app_essay_part_1/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/hf4awf/how_to_approach_the_common_app_essay_part_2/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/hfqung/how_to_approach_the_common_app_essay_part_3/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/hgbcai/how_to_approach_the_common_app_essay_part_4/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/95hbdn/my_worldending_guide_to_the_college_essay/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/ab9f9f/last_minute_why_x_supplement_advice_from_a/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/97x25e/an_analysis_of_why_the_mundane_topic_seems_to/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/fxxlv2/essay_advice_from_a_stanford_2024_admit/',
    'https://www.reddit.com/r/ApplyingToCollege/comments/ea5tzl/personal_statement_tips/',
    'https://www.reddit.com/r/CollegeEssayReview/comments/ddyj9l/giving_away_the_secret_sauce_how_to_make_your/',
  ];
  
  // Function to extract post title and body from a Reddit link
  async function extractRedditPostData(url) {
    // Extract the post ID and subreddit from the link
    const regex = /https:\/\/www.reddit.com\/r\/([^/]+)\/comments\/([^/]+)\/([^/]+)/;
    const match = url.match(regex);
    if (!match) {
      console.error('Invalid Reddit link:', url);
      return;
    }
  
    const [, subreddit, postId] = match;
  
    // Make a request to the Reddit API
    const response = await fetch(`https://www.reddit.com/r/${subreddit}/comments/${postId}.json`);
    const data = await response.json();
  
    // Extract post title and body from the API response
    const post = data[0].data.children[0].data;
    const title = post.title;
    const body = post.selftext;
  
    console.log('Post Title:', title);
    console.log('Post Body:', body);
    console.log('******************************************************************************************************** End of Post ********************************************************************************************************')
  }
  
  // Process each Reddit link
  redditLinks.forEach((link) => {
    extractRedditPostData(link);
  });
  