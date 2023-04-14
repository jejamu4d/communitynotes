import time

import numpy as np


# Store the timestamp at which the constants module is initialized.  Note
# that module initialization occurs only once regardless of how many times
# the module is imported (see link below).  Storing a designated timestamp
# as a constant allow us to:
#  -Use a consistent notion of "now" throughout scorer execution.
#  -Overwrite "now" when system testing to reduce spurious diffs.
#
# https://docs.python.org/3/tutorial/modules.html#more-on-modules
epochMillis = 1000 * time.time()

maxTrainError = 0.09

# Explanation Tags
minRatingsToGetTag = 2
minTagsNeededForStatus = 2
tagPercentileForNormalization = 40

# Data Filenames
scoredNotesOutputPath = "scoredNotes.tsv"
enrollmentInputPath = "userEnrollment-00000.tsv"
notesInputPath = "notes-00000.tsv"
ratingsInputPath = "ratings-00000.tsv"
noteStatusHistoryInputPath = "noteStatusHistory-00000.tsv"

# TSV Column Names
participantIdKey = "participantId"
helpfulKey = "helpful"
notHelpfulKey = "notHelpful"
helpfulnessLevelKey = "helpfulnessLevel"
createdAtMillisKey = "createdAtMillis"
summaryKey = "summary"
authorTopNotHelpfulTagValues = "authorTopNotHelpfulTagValues"
modelingPopulationKey = "modelingPopulation"

# TSV Values
notHelpfulValueTsv = "NOT_HELPFUL"
somewhatHelpfulValueTsv = "SOMEWHAT_HELPFUL"
helpfulValueTsv = "HELPFUL"
notesSaysTweetIsMisleadingKey = "MISINFORMED_OR_POTENTIALLY_MISLEADING"
noteSaysTweetIsNotMisleadingKey = "NOT_MISLEADING"

# Fields Transformed From the Raw Data
helpfulNumKey = "helpfulNum"
ratingCreatedBeforeMostRecentNMRLabelKey = "ratingCreatedBeforeMostRecentNMRLabel"
ratingCreatedBeforePublicTSVReleasedKey = "ratingCreatedBeforePublicTSVReleased"

# Timestamps
deletedNoteTombstonesLaunchTime = 1652918400000  # May 19, 2022 UTC
notMisleadingUILaunchTime = 1664755200000  # October 3, 2022 UTC
publicTSVTimeDelay = 172800000  # 48 hours

# Explanation Tags
tagCountsKey = "tagCounts"
tiebreakOrderKey = "tiebreakOrder"
firstTagKey = "firstTag"
secondTagKey = "secondTag"
activeFilterTagsKey = "activeFilterTags"

# Contributor Counts
successfulRatingHelpfulCount = "successfulRatingHelpfulCount"
successfulRatingNotHelpfulCount = "successfulRatingNotHelpfulCount"
successfulRatingTotal = "successfulRatingTotal"
unsuccessfulRatingHelpfulCount = "unsuccessfulRatingHelpfulCount"
unsuccessfulRatingNotHelpfulCount = "unsuccessfulRatingNotHelpfulCount"
unsuccessfulRatingTotal = "unsuccessfulRatingTotal"
ratingsAwaitingMoreRatings = "ratingsAwaitingMoreRatings"
ratedAfterDecision = "ratedAfterDecision"
notesCurrentlyRatedHelpful = "notesCurrentlyRatedHelpful"
notesCurrentlyRatedNotHelpful = "notesCurrentlyRatedNotHelpful"
notesAwaitingMoreRatings = "notesAwaitingMoreRatings"

# Meta Scoring Columns
finalRatingStatusKey = "finalRatingStatus"
unlockedRatingStatusKey = "unlockedRatingStatus"
metaScorerActiveRulesKey = "metaScorerActiveRules"
decidedByKey = "decidedBy"

# Internal Scoring Columns.  These columns should be renamed before writing to disk.
internalNoteInterceptKey = "internalNoteIntercept"
internalRaterInterceptKey = "internalRaterIntercept"
internalNoteFactorKeyBase = "internalNoteFactor"
internalRaterFactorKeyBase = "internalRaterFactor"
internalRatingStatusKey = "internalRatingStatus"
internalActiveRulesKey = "internalActiveRules"


def note_factor_key(i):
  return internalNoteFactorKeyBase + str(i)


def rater_factor_key(i):
  return internalRaterFactorKeyBase + str(i)


internalNoteFactor1Key = note_factor_key(1)
internalRaterFactor1Key = rater_factor_key(1)

# Output Scoring Columns.
# Core Model
coreNoteInterceptKey = "coreNoteIntercept"
coreNoteFactor1Key = "coreNoteFactor1"
coreRaterInterceptKey = "coreRaterIntercept"
coreRaterFactor1Key = "coreRaterFactor1"
coreRatingStatusKey = "coreRatingStatus"
coreActiveRulesKey = "coreActiveRules"
coreNoteInterceptMaxKey = "coreNoteInterceptMax"
coreNoteInterceptMinKey = "coreNoteInterceptMin"
# Expansion Model
expansionNoteInterceptKey = "expansionNoteIntercept"
expansionNoteFactor1Key = "expansionNoteFactor1"
expansionRatingStatusKey = "expansionRatingStatus"
expansionNoteInterceptMaxKey = "expansionNoteInterceptMax"
expansionNoteInterceptMinKey = "expansionNoteInterceptMin"
# Coverage Model
coverageNoteInterceptKey = "coverageNoteIntercept"
coverageNoteFactor1Key = "coverageNoteFactor1"
coverageRatingStatusKey = "coverageRatingStatus"
coverageNoteInterceptMaxKey = "coverageNoteInterceptMax"
coverageNoteInterceptMinKey = "coverageNoteInterceptMin"

# Ids and Indexes
noteIdKey = "noteId"
tweetIdKey = "tweetId"
classificationKey = "classification"
noteAuthorParticipantIdKey = "noteAuthorParticipantId"
raterParticipantIdKey = "raterParticipantId"

# Aggregations
noteCountKey = "noteCount"
ratingCountKey = "ratingCount"
numRatingsKey = "numRatings"
numRatingsLast28DaysKey = "numRatingsLast28"

# Helpfulness Score Keys
crhRatioKey = "CRHRatio"
crnhRatioKey = "CRNHRatio"
crhCrnhRatioDifferenceKey = "crhCrnhRatioDifference"
meanNoteScoreKey = "meanNoteScore"
raterAgreeRatioKey = "raterAgreeRatio"
ratingAgreesWithNoteStatusKey = "ratingAgreesWithNoteStatus"
aboveHelpfulnessThresholdKey = "aboveHelpfulnessThreshold"

# Note Status Labels
currentlyRatedHelpful = "CURRENTLY_RATED_HELPFUL"
currentlyRatedNotHelpful = "CURRENTLY_RATED_NOT_HELPFUL"
needsMoreRatings = "NEEDS_MORE_RATINGS"

# Boolean Note Status Labels
currentlyRatedHelpfulBoolKey = "crhBool"
currentlyRatedNotHelpfulBoolKey = "crnhBool"
awaitingMoreRatingsBoolKey = "awaitingBool"

helpfulTagsAndTieBreakOrder = [
  (0, "helpfulOther"),
  (8, "helpfulInformative"),
  (7, "helpfulClear"),
  (3, "helpfulEmpathetic"),
  (4, "helpfulGoodSources"),
  (2, "helpfulUniqueContext"),
  (5, "helpfulAddressesClaim"),
  (6, "helpfulImportantContext"),
  (1, "helpfulUnbiasedLanguage"),
]
helpfulTagsTSVOrder = [tag for (tiebreakOrder, tag) in helpfulTagsAndTieBreakOrder]
helpfulTagsAndTypesTSVOrder = [(tag, np.int64) for tag in helpfulTagsTSVOrder]
helpfulTagsTiebreakOrder = [tag for (tiebreakOrder, tag) in sorted(helpfulTagsAndTieBreakOrder)]

# NOTE: Always add new tags to the end of this list, and *never* change the order of
# elements which are already in the list to maintain compatibility with
# BirdwatchNoteNotHelpfulTags.get in Scala.

notHelpfulSpamHarassmentOrAbuseTagKey = "notHelpfulSpamHarassmentOrAbuse"
notHelpfulArgumentativeOrBiasedTagKey = "notHelpfulArgumentativeOrBiased"
notHelpfulHardToUnderstandKey = "notHelpfulHardToUnderstand"
notHelpfulNoteNotNeededKey = "notHelpfulNoteNotNeeded"

notHelpfulTagsAndTieBreakOrder = [
  (0, "notHelpfulOther"),
  (8, "notHelpfulIncorrect"),
  (2, "notHelpfulSourcesMissingOrUnreliable"),
  (4, "notHelpfulOpinionSpeculationOrBias"),
  (5, "notHelpfulMissingKeyPoints"),
  (12, "notHelpfulOutdated"),
  (10, notHelpfulHardToUnderstandKey),
  (7, notHelpfulArgumentativeOrBiasedTagKey),
  (9, "notHelpfulOffTopic"),
  (11, notHelpfulSpamHarassmentOrAbuseTagKey),
  (1, "notHelpfulIrrelevantSources"),
  (3, "notHelpfulOpinionSpeculation"),
  (6, notHelpfulNoteNotNeededKey),
]
notHelpfulTagsTSVOrder = [tag for (tiebreakOrder, tag) in notHelpfulTagsAndTieBreakOrder]
notHelpfulTagsAndTypesTSVOrder = [(tag, np.int64) for tag in notHelpfulTagsTSVOrder]
notHelpfulTagsTiebreakOrder = [
  tag for (tiebreakOrder, tag) in sorted(notHelpfulTagsAndTieBreakOrder)
]
notHelpfulTagsTiebreakMapping = {
  tag: priority for (priority, tag) in notHelpfulTagsAndTieBreakOrder
}
notHelpfulTagsEnumMapping = {
  tag: idx for (idx, (_, tag)) in enumerate(notHelpfulTagsAndTieBreakOrder)
}
adjustedSuffix = "Adjusted"
notHelpfulTagsAdjustedColumns = [f"{column}{adjustedSuffix}" for column in notHelpfulTagsTSVOrder]
ratioSuffix = "Ratio"
notHelpfulTagsAdjustedRatioColumns = [
  f"{column}{ratioSuffix}" for column in notHelpfulTagsAdjustedColumns
]
ratingWeightKey = "ratingWeight"

misleadingTags = [
  "misleadingOther",
  "misleadingFactualError",
  "misleadingManipulatedMedia",
  "misleadingOutdatedInformation",
  "misleadingMissingImportantContext",
  "misleadingUnverifiedClaimAsFact",
  "misleadingSatire",
]
misleadingTagsAndTypes = [(tag, np.int64) for tag in misleadingTags]

notMisleadingTags = [
  "notMisleadingOther",
  "notMisleadingFactuallyCorrect",
  "notMisleadingOutdatedButNotWhenWritten",
  "notMisleadingClearlySatire",
  "notMisleadingPersonalOpinion",
]
notMisleadingTagsAndTypes = [(tag, np.int64) for tag in notMisleadingTags]


noteTSVColumnsAndTypes = (
  [
    (noteIdKey, np.int64),
    (noteAuthorParticipantIdKey, np.object),
    (createdAtMillisKey, np.int64),
    (tweetIdKey, np.int64),
    (classificationKey, np.object),
    ("believable", np.object),
    ("harmful", np.object),
    ("validationDifficulty", np.object),
  ]
  + misleadingTagsAndTypes
  + notMisleadingTagsAndTypes
  + [
    ("trustworthySources", np.int64),
    (summaryKey, np.object),
  ]
)
noteTSVColumns = [col for (col, dtype) in noteTSVColumnsAndTypes]
noteTSVTypes = [dtype for (col, dtype) in noteTSVColumnsAndTypes]
noteTSVTypeMapping = {col: dtype for (col, dtype) in noteTSVColumnsAndTypes}

ratingTSVColumnsAndTypes = (
  [
    (noteIdKey, np.int64),
    (raterParticipantIdKey, np.object),
    (createdAtMillisKey, np.int64),
    ("version", np.int64),
    ("agree", np.int64),
    ("disagree", np.int64),
    (helpfulKey, np.int64),
    (notHelpfulKey, np.int64),
    (helpfulnessLevelKey, np.object),
  ]
  + helpfulTagsAndTypesTSVOrder
  + notHelpfulTagsAndTypesTSVOrder
)

ratingTSVColumns = [col for (col, dtype) in ratingTSVColumnsAndTypes]
ratingTSVTypes = [dtype for (col, dtype) in ratingTSVColumnsAndTypes]
ratingTSVTypeMapping = {col: dtype for (col, dtype) in ratingTSVColumnsAndTypes}


timestampMillisOfNoteFirstNonNMRLabelKey = "timestampMillisOfFirstNonNMRStatus"
firstNonNMRLabelKey = "firstNonNMRStatus"
timestampMillisOfNoteCurrentLabelKey = "timestampMillisOfCurrentStatus"
currentLabelKey = "currentStatus"
timestampMillisOfNoteMostRecentNonNMRLabelKey = "timestampMillisOfLatestNonNMRStatus"
mostRecentNonNMRLabelKey = "mostRecentNonNMRStatus"
timestampMillisOfStatusLockKey = "timestampMillisOfStatusLock"
lockedStatusKey = "lockedStatus"
timestampMillisOfRetroLockKey = "timestampMillisOfRetroLock"

noteStatusHistoryTSVColumnsAndTypes = [
  (noteIdKey, np.int64),
  (noteAuthorParticipantIdKey, np.object),
  (createdAtMillisKey, np.int64),
  (timestampMillisOfNoteFirstNonNMRLabelKey, np.double),  # double because nullable.
  (firstNonNMRLabelKey, np.object),
  (timestampMillisOfNoteCurrentLabelKey, np.double),  # double because nullable.
  (currentLabelKey, np.object),
  (timestampMillisOfNoteMostRecentNonNMRLabelKey, np.double),  # double because nullable.
  (mostRecentNonNMRLabelKey, np.object),
  (timestampMillisOfStatusLockKey, np.double),  # double because nullable.
  (lockedStatusKey, np.object),
  (timestampMillisOfRetroLockKey, np.double),  # double because nullable.
]
noteStatusHistoryTSVColumns = [col for (col, dtype) in noteStatusHistoryTSVColumnsAndTypes]
noteStatusHistoryTSVTypes = [dtype for (col, dtype) in noteStatusHistoryTSVColumnsAndTypes]
noteStatusHistoryTSVTypeMapping = {
  col: dtype for (col, dtype) in noteStatusHistoryTSVColumnsAndTypes
}

# Earn In + Earn Out
enrollmentState = "enrollmentState"
successfulRatingNeededToEarnIn = "successfulRatingNeededToEarnIn"
timestampOfLastStateChange = "timestampOfLastStateChange"
timestampOfLastEarnOut = "timestampOfLastEarnOut"
authorTopNotHelpfulTagValues = "authorTopNotHelpfulTagValues"
maxHistoryEarnOut = 5
successfulRatingHelpfulCount = "successfulRatingHelpfulCount"
earnedIn = "earnedIn"
atRisk = "atRisk"
earnedOutNoAcknowledge = "earnedOutNoAcknowledge"
earnedOutAcknowledged = "earnedOutAcknowledged"
newUser = "newUser"
isAtRiskCRNHCount = 2
ratingImpactForEarnIn = 5
ratingImpact = "ratingImpact"
enrollmentStateToThrift = {
  earnedIn: 0,
  atRisk: 1,
  earnedOutNoAcknowledge: 2,
  earnedOutAcknowledged: 3,
  newUser: 4,
}
emergingWriterDays = 28
isEmergingWriterKey = "isEmergingWriter"
emergingMeanNoteScore = 0.3
emergingRatingCount = 10
aggregateRatingReceivedTotal = "aggregateRatingReceivedTotal"
core = "CORE"
expansion = "EXPANSION"

userEnrollmentTSVColumnsAndTypes = [
  (participantIdKey, np.str),
  (enrollmentState, np.str),
  (successfulRatingNeededToEarnIn, np.int64),
  (timestampOfLastStateChange, np.int64),
  (timestampOfLastEarnOut, np.double),  # double because nullable.
  (modelingPopulationKey, np.str),
]
userEnrollmentTSVColumns = [col for (col, _) in userEnrollmentTSVColumnsAndTypes]
userEnrollmentTSVTypes = [dtype for (_, dtype) in userEnrollmentTSVColumnsAndTypes]
userEnrollmentTSVTypeMapping = {col: dtype for (col, dtype) in userEnrollmentTSVColumnsAndTypes}

noteInterceptMaxKey = "internalNoteIntercept_max"
noteInterceptMinKey = "internalNoteIntercept_min"
noteParameterUncertaintyTSVMainColumnsAndTypes = [
  (noteInterceptMaxKey, np.double),
  (noteInterceptMinKey, np.double),
]
noteParameterUncertaintyTSVAuxColumnsAndTypes = [
  ("internalNoteFactor1_max", np.double),
  ("internalNoteFactor1_median", np.double),
  ("internalNoteFactor1_min", np.double),
  ("internalNoteFactor1_refit_orig", np.double),
  ("internalNoteIntercept_median", np.double),
  ("internalNoteIntercept_refit_orig", np.double),
  ("ratingCount_all", np.int64),
  ("ratingCount_neg_fac", np.int64),
  ("ratingCount_pos_fac", np.int64),
]
noteParameterUncertaintyTSVColumnsAndTypes = (
  noteParameterUncertaintyTSVAuxColumnsAndTypes + noteParameterUncertaintyTSVMainColumnsAndTypes
)
noteParameterUncertaintyTSVColumns = [
  col for (col, _) in noteParameterUncertaintyTSVColumnsAndTypes
]
noteParameterUncertaintyTSVAuxColumns = [
  col for (col, _) in noteParameterUncertaintyTSVAuxColumnsAndTypes
]
noteParameterUncertaintyTSVMainColumns = [
  col for (col, _) in noteParameterUncertaintyTSVMainColumnsAndTypes
]
noteParameterUncertaintyTSVTypes = [
  dtype for (_, dtype) in noteParameterUncertaintyTSVColumnsAndTypes
]
noteParameterUncertaintyTSVTypeMapping = {
  col: dtype for (col, dtype) in noteParameterUncertaintyTSVColumnsAndTypes
}

auxiliaryScoredNotesTSVColumns = (
  [
    noteIdKey,
    ratingWeightKey,
    numRatingsKey,
    createdAtMillisKey,
    noteAuthorParticipantIdKey,
    awaitingMoreRatingsBoolKey,
    numRatingsLast28DaysKey,
    currentLabelKey,
    currentlyRatedHelpfulBoolKey,
    currentlyRatedNotHelpfulBoolKey,
    unlockedRatingStatusKey,
  ]
  + helpfulTagsTSVOrder
  + notHelpfulTagsTSVOrder
  + notHelpfulTagsAdjustedColumns
  + notHelpfulTagsAdjustedRatioColumns
)

noteModelOutputTSVColumnsAndTypes = [
  (noteIdKey, np.int64),
  (coreNoteInterceptKey, np.double),
  (coreNoteFactor1Key, np.double),
  (finalRatingStatusKey, np.str),
  (firstTagKey, np.str),
  (secondTagKey, np.str),
  # Note that this column was formerly named "activeRules" and the name is now
  # updated to "coreActiveRules".  The data values remain the compatible,
  # but the new column only contains rules that ran when deciding status based on
  # the core model.
  (coreActiveRulesKey, np.str),
  (activeFilterTagsKey, np.str),
  (classificationKey, np.str),
  (createdAtMillisKey, np.int64),
  (coreRatingStatusKey, np.str),
  (metaScorerActiveRulesKey, np.str),
  (decidedByKey, np.str),
  (expansionNoteInterceptKey, np.double),
  (expansionNoteFactor1Key, np.double),
  (expansionRatingStatusKey, np.str),
  (coverageNoteInterceptKey, np.double),
  (coverageNoteFactor1Key, np.double),
  (coverageRatingStatusKey, np.str),
  (coreNoteInterceptMinKey, np.double),
  (coreNoteInterceptMaxKey, np.double),
  (expansionNoteInterceptMinKey, np.double),
  (expansionNoteInterceptMaxKey, np.double),
  (coverageNoteInterceptMinKey, np.double),
  (coverageNoteInterceptMaxKey, np.double),
]
noteModelOutputTSVColumns = [col for (col, dtype) in noteModelOutputTSVColumnsAndTypes]
noteModelOutputTSVTypeMapping = {col: dtype for (col, dtype) in noteModelOutputTSVColumnsAndTypes}

raterModelOutputTSVColumnsAndTypes = [
  (raterParticipantIdKey, np.int64),
  (coreRaterInterceptKey, np.double),
  (coreRaterFactor1Key, np.double),
  (crhCrnhRatioDifferenceKey, np.double),
  (meanNoteScoreKey, np.double),
  (raterAgreeRatioKey, np.double),
  (successfulRatingHelpfulCount, np.int64),
  (successfulRatingNotHelpfulCount, np.int64),
  (successfulRatingTotal, np.int64),
  (unsuccessfulRatingHelpfulCount, np.int64),
  (unsuccessfulRatingNotHelpfulCount, np.int64),
  (unsuccessfulRatingTotal, np.int64),
  (ratingsAwaitingMoreRatings, np.int64),
  (ratedAfterDecision, np.int64),
  (notesCurrentlyRatedHelpful, np.int64),
  (notesCurrentlyRatedNotHelpful, np.int64),
  (notesAwaitingMoreRatings, np.int64),
  (enrollmentState, np.int32),
  (successfulRatingNeededToEarnIn, np.int64),
  (authorTopNotHelpfulTagValues, np.str),
  (timestampOfLastStateChange, np.int64),
  (aboveHelpfulnessThresholdKey, np.bool_),
  (isEmergingWriterKey, np.bool_),
  (aggregateRatingReceivedTotal, np.int64),
  (timestampOfLastEarnOut, np.double),
]
raterModelOutputTSVColumns = [col for (col, dtype) in raterModelOutputTSVColumnsAndTypes]
raterModelOutputTSVTypeMapping = {col: dtype for (col, dtype) in raterModelOutputTSVColumnsAndTypes}
