# Run with: ruby test/publication_author_initials_test.rb
require 'minitest/autorun'
require 'liquid'

module PublicationInitialsFilters
  def regex_replace(input, pattern, replacement)
    input.to_s.gsub(Regexp.new(pattern), replacement)
  end
end

Liquid::Template.register_filter(PublicationInitialsFilters)

class PublicationAuthorInitialsTest < Minitest::Test
  TEMPLATE = File.read(File.expand_path('../_includes/publication_author_initials.liquid', __dir__))

  def initials(first, last = 'Lee')
    Liquid::Template.parse(TEMPLATE, error_mode: :strict).render!(
      'include' => { 'first' => first, 'last' => last }
    ).strip
  end

  def test_full_names_and_existing_initials_share_one_format
    assert_equal 'D.', initials('Dohyeon')
    assert_equal 'H.', initials('Herve', 'Hugonnet')
    assert_equal 'D. M.', initials('DM', 'Ryu')
    assert_equal 'D. M.', initials('D. M.', 'Ryu')
    assert_equal 'M. S.', initials('M. Shahrooz', 'Amin')
  end

  def test_known_yongkeun_park_variants
    ['YongKeun', 'Yongkeun', 'Yong Keun', 'YoungKeun', 'YougKeun', 'YK', 'Y. K.'].each do |given|
      assert_equal 'Y. K.', initials(given, 'Park')
    end
    assert_equal 'Y.', initials('Y', 'Park') # Do not expand an ambiguous initial.
  end

  def test_hyphens_accents_and_empty_given_names
    assert_equal 'S.-M.', initials('Sang-min')
    assert_equal 'S.-M.', initials('S-M')
    assert_equal 'É.', initials('Élodie')
    assert_equal '', initials('')
  end
end
