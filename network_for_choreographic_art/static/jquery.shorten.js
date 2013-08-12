/**
 * @author Eric Schrijver
 */

(function($) {
    $.fn.shorten = function(n) {
        n = typeof(n) != 'undefined' ? n : 16;
        this.each(function(index) {
            $(this).attr('id', index);
            allText = $(this).text().split(' ');
            if (allText.length > n) {
                shownText = allText.slice(0, n).join(' ');
                hiddenText = allText.slice(n).join(' ');
                $(this).html(shownText + '<span class="expand">…</span>' + '&nbsp;&nbsp;<a href="#" class="expand">more</a>' + ' <span class="more">' + hiddenText + '</span>&nbsp;&nbsp;<a href="#" class="contract">less</a>');
                $('#' + index + ' .more').toggle();
                $('#' + index + ' .contract').toggle();

                $('#' + index + " .expand, " + '#' + index + " .contract").click(function(event) {
                    event.preventDefault();
                    $('#' + index + ' .more').toggle();
                    $('#' + index + ' .expand').toggle();
                    $('#' + index + ' .contract').toggle();
                });
            }
        });
    };
})(jQuery)