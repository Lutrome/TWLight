#!/usr/bin/perl

# Checks for localization issues.
# https://phabricator.wikimedia.org/T255167

use strict;
use warnings;
use Term::ANSIColor;

# Experimental features add warning output, which we don't want in our CI logs.
no warnings 'experimental';
# Exit code.
my $code = 0;

# We take a file path as the first argument.
my $filename = $ARGV[0];
my $input = do { local $/; <> };

# Check for newlines that can cause message mismatches with translatewiki.
my @newline_errors = ($input =~ /(?<!_)_\(\n(([ \t]*)?"[^\n]*"\n?)*([ \t]*)\)/sg);
foreach my $match (@newline_errors) {
    my $message = "ugettext messages should't be preceded by a newline";
    print_error($message, $filename, $input, $match);
}

# Check for messages not preceded by a translator comment with a max length of 240 characters.
# Note the variable-width negative lookbehind, which has experimental support.
# We're keeping the pattern within the limitations of the engine.
my @comment_errors = ($input =~ /(?<!# Translators:[^\n]{1,240}\n)([^\n]*(?<!_)_\((([ \t]*)?"[^\n]*"\n?)*([ \t]*)\)[^\n]\n)/sg);
foreach my $match (@comment_errors) {
    my $message = 'Missing or overlong (> 240 chars) translator comment';
    print_error($message, $filename, $input, $match);
}

# Prints errors. Surpise!
sub print_error {
    my $message = $_[0];
    my $filename = $_[1];
    my @input = split /\n/, $_[2];
    # Drop newlines that complicate comparison.
    chomp(my $match = $_[3]);
    # Drop zero-length matches.
    if (length($match) > 0) {
        # Loop through the input lines
        for my $i (0 .. $#input) {
            # Print the error with line number when we get to the match.
            if ("$input[$i]" eq "$match") {
                my $number = $i + 1;
                $code = 1;
                print colored("ERROR: $message\n$filename:$number\n$match\n", 'red');
            }
        }
    }
}

exit $code;
